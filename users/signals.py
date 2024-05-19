# users/signals.py
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from .models import Kurator, Group

@receiver(m2m_changed, sender=Kurator.groups.through)
def validate_unique_groups(sender, instance, action, **kwargs):
    if action == 'pre_add':
        for group_id in kwargs.get('pk_set', []):
            group = Group.objects.get(pk=group_id)
            if Kurator.objects.filter(groups=group).exclude(pk=instance.pk).exists():
                raise ValidationError(f"Группа {group.group_name} уже назначена другому куратору.")