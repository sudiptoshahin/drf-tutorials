from django.db import models
from django.contrib.auth.models import BaseUserManager, UserManager, User
from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.db.models.signals import post_save
from django.dispatch import receiver


class Artist(models.Model):
    name = models.CharField(max_length=10)
    

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_person = models.CharField(max_length=64)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,
#                                 related_name='profile')
#     profile_picture = models.ImageField(upload_to='profile-picture/',
#                                         blank=True, null=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     birthdate = models.DateField(blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     present_address = models.CharField(max_length=255, blank=True, null=True)
#     permanent_address = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return f"{self.user.username}'s Profile"

# class Profile(User):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,
#                                 related_name='profile')
#     profile_picture = models.ImageField(upload_to='profile-picture/',
#                                         blank=True, null=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     birthdate = models.DateField(blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     present_address = models.CharField(max_length=255, blank=True, null=True)
#     permanent_address = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return f"{self.user.username}'s Profile"
    
#     # @receiver(post_save, sender=User)
#     # def create_user_profile(sender, instance, created, **kwargs):
#     #     if created:
#     #         Profile.objects.create(user=instance)

#     # @receiver(post_save, sender=User)
#     # def save_user_profile(sender, instance, **kwargs):
#     #     instance.profile.save()
    
#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             # print("create",sender, instance,created,**kwargs)
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         # print("save",sender, instance,**kwargs)
#         instance.profile.save()


# manager
# class HeadManager(BaseUserManager):
#   .................................


# Authentication Backends
# class UserAdmin(BaseBackend, ModelBackend):
#   .....................
