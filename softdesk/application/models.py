from django.db import models
from authentication.models import User


class Project(models.Model):
    TYPE_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('ios', 'iOS'),
        ('android', 'Android'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=254)
    type = models.CharField(choices=TYPE_CHOICES, max_length=30)


class Contributor(models.Model):
    PERMISSION_CHOICES = [
        ('author', 'Author'),
        ('contributor', 'Contributor'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(
        choices=PERMISSION_CHOICES,
        max_length=30,
        default='contributor'
        )


class Issue(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    TAG_CHOICES = [
        ('bug', 'Bug'),
        ('improvement', 'Improvement'),
        ('task', 'Task'),
    ]
    STATUS_CHOICES = [
        ('to_do', 'To do'),
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=254)
    tag = models.CharField(choices=TAG_CHOICES, max_length=30)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='author_issue'
        )
    assignee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=254)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

