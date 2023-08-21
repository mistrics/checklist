from django.db import models
from django.conf import settings


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Department(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Checklist(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    departments = models.ManyToManyField(Department)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class ChecklistInstance(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='checklist_instances')
    date_completed = models.DateField()
    status = models.CharField(max_length=20, default='incomplete')
    
    def __str__(self):
        return f"{self.checklist.title} - {self.supervisor.username}"
    
class TaskInstance(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    checklist_instance = models.ForeignKey(ChecklistInstance, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    comments = models.TextField(blank=True)
    media = models.ImageField(upload_to='task_media/', blank=True, null=True)

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class ScheduledTask(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

class Report(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_generated = models.DateField(auto_now_add=True)
    content = models.TextField()

class MediaFile(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media_files/')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)