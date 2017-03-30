from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    school = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, blank=True)

    def is_male(self):
    	if self.gender == 'M' or self.gender == 'm':
    		return True
    	else:
    		return False
    			

    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return 'Name: {}'.format(name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
