import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

# Unique dispatch ID to prevent duplicate signals
unique_uid = uuid.uuid4()


# Create a use profile when a user is registered
@receiver(post_save, sender=User, dispatch_uid=unique_uid)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Save the profile
@receiver(post_save, sender=User, dispatch_uid=unique_uid)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
