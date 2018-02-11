import json

from django.http import Http404
from django import http
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings

from .utils import resolve_google_oauth
from .models import GoogleUser, UserProxy
from .serializers import GoogleUserSerializer, UserSerializer


class LoginRequiredMixin(object):

    '''View mixin which requires that the user is authenticated.'''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class ExemptCSRFMixn(object):
    """View mixin defined to exempt csrf."""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ExemptCSRFMixn, self).dispatch(
    request, *args, **kwargs)


class DashBoardView(TemplateView):

    template_name = 'index.html'


class GoogleLoginView(APIView):

    permission_classes = (AllowAny,)

    def get_oauth_token(self, userproxy, google_user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(userproxy)
        token = jwt_encode_handler(payload)

        serializer = GoogleUserSerializer(google_user)

        body = {
          'token': token,
          'user': serializer.data,
        }

        return body

    def post(self, request, format=None):

        idinfo = resolve_google_oauth(request)

        # if it is a returning user.
        try:
            google_user = GoogleUser.objects.get(google_id=idinfo['sub'])
            google_user.check_diff(idinfo)
            userproxy = UserProxy.objects.get(id=google_user.app_user.id)
            userproxy.check_diff(idinfo)

        except GoogleUser.DoesNotExist:
            # proceed to create the user
            email_length = len(idinfo['email'])
            hd_length = len(idinfo['hd']) + 1
            userproxy = UserProxy(
                username=idinfo['email'][:email_length - hd_length],
                email=idinfo['email'],
                first_name=idinfo['given_name'],
                last_name=idinfo['family_name'],
            )
            userproxy.save()
            google_user = GoogleUser(google_id=idinfo['sub'],
                                     app_user=userproxy,
                                     appuser_picture=idinfo['picture'],
                                     )
            google_user.save()

        response = self.get_oauth_token(userproxy, google_user)
        return Response(response, status=status.HTTP_200_OK)





