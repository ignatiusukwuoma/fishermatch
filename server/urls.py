from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from server import views

urlpatterns = [
    url(r'^auth/login/?$', views.GoogleLoginView.as_view(),
        name='auth_login'),

    url(r'^auth/token/?$', obtain_jwt_token),

    url(r'^auth/token-verify/?$', verify_jwt_token),

    url(r'^home/?$',
        views.DashBoardView.as_view(),
        name='dashboard'),
]
