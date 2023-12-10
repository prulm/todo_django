from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Note

@receiver(pre_save, sender=Note)
def set_updated_on(sender, instance, **kwargs):
    if instance._state.adding:
        instance.updated_on = None
    else:
        instance.updated_on = timezone.now()