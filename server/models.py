from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class BaseInfo(models.Model):
    """Base class containing all models common information."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Define Model as abstract."""

        abstract = True


class UserProxy(User):
    """Class defined to create a proxy for the user model.
        Changes made to this model directly affects the User model
        and vice-versa. Model allows methods to be defined on the User model
        without altering the user model itself.
        https://docs.djangoproject.com/en/1.11/topics/db/models/
    """
    class Meta:
        proxy = True
        auto_created = True

    def check_diff(self, idinfo):
        """
        Check for differences between request/idinfo and model data.
            Args:
                idinfo: data passed in from post method.
        """
        email_length = len(idinfo['email'])
        hd_length = len(idinfo['hd']) + 1
        data = {
                "username": idinfo['email'][:email_length - hd_length],
                "email": idinfo["email"],
                "first_name": idinfo['given_name'],
                "last_name": idinfo['family_name'],
            }

        for field in data:
            if getattr(self, field) != data[field] and data[field] != '':
                setattr(self, field, data[field])
        self.save()


class GoogleUser(models.Model):
    google_id = models.CharField(max_length=60, unique=True)

    app_user = models.OneToOneField(User, related_name='user',
                                    on_delete=models.CASCADE)
    appuser_picture = models.TextField()

    def check_diff(self, idinfo):
        """Check for differences between request/idinfo and model data.
            Args:
                idinfo: data passed in from post method.
        """
        data = {
                "appuser_picture": idinfo['picture'],
            }

        for field in data:
            if getattr(self, field) != data[field] and data[field] != '':
                setattr(self, field, data[field])
        self.save()

    def __str__(self):
        return "@{}".format(self.app_user.username)


class UserProfile(models.Model):
    """Class that defines user profile model.
    Attributes: user
    """

    # more fields here, not sure for now.
    user = models.OneToOneField(User)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


def create_user_profile(sender, instance, created, **kwargs):
    """Creates the user profile for a given User instance.

       Args: sender, instance, created,
       Sender: The model class,
       Instance: The actual instance being saved,
       Created: Boolean that defaults to True if user is created
    """
    if created:
        UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User,
                      dispatch_uid=create_user_profile)