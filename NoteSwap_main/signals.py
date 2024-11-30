from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# Function to create a UserProfile automatically when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Check if this is a new user
        UserProfile.objects.create(user=instance)  # Create a UserProfile and associate it with the new user

# Function to save the UserProfile when the User is saved (updated or modified)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # Save the related UserProfile every time the User is saved
