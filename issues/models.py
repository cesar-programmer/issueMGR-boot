from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# Assuming 'Projects' model is defined elsewhere in your models.py
# from .models import Projects

User = get_user_model()

class Issue(models.Model):
    class Status(models.TextChoices):
        TODO = 'to do', _('To Do')
        IN_PROGRESS = 'in progress', _('In Progress')
        DONE = 'done', _('Done')

    class Priority(models.TextChoices):
        LOW = 'low', _('Low')
        MEDIUM = 'medium', _('Medium')
        HIGH = 'high', _('High')

    summary = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO
    )
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.LOW
    )
    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reported_issues'
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_issues'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary
