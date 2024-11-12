from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Permission
from .models import Restaurant

@receiver(post_save, sender=Restaurant)
def assign_permissions(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename='add_dish')
        instance.user.user_permissions.add(permission)