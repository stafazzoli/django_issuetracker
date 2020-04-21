from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    category = models.ForeignKey(
        ProjectCategory, null=True,
        related_name='projects',
        on_delete=models.SET_NULL
    )
    created_by = models.ForeignKey(
        User,
        related_name='projects',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'pk': self.pk})


class Issue(models.Model):
    STATUS_CHOICES = (
        ('CR', 'Created'),
        ('IP', 'In Progress'),
        ('DN', 'Done'),
        ('CN', 'Cancelled')
    )
    PRIORITY_CHOICES = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='M', max_length=1)
    status = models.CharField(choices=STATUS_CHOICES, default='CR', max_length=2)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, editable=False)
    attachment = models.FileField(upload_to='issues/%Y/%m', blank=True, null=True)
    project = models.ForeignKey(
        Project, related_name='issues', on_delete=models.CASCADE
    )
    reporter = models.ForeignKey(
        User, related_name='reporter_issues', on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        User, related_name='assignee_issues', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:issue_detail', kwargs={'pk': self.pk})
