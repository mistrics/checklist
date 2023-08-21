from django.contrib import admin
from .models import Organization, Department, Checklist, Task, ChecklistInstance, TaskInstance, Notification, ScheduledTask, Report, MediaFile

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_per_page = 20

    fieldsets = (
        ('Organization Information', {
            'fields': ('name', 'description'),
        }),
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('title', 'frequency')
    filter_horizontal = ('departments',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'checklist', 'order')

@admin.register(ChecklistInstance)
class ChecklistInstanceAdmin(admin.ModelAdmin):
    list_display = ('checklist', 'supervisor', 'date_completed', 'status')

@admin.register(TaskInstance)
class TaskInstanceAdmin(admin.ModelAdmin):
    list_display = ('task', 'checklist_instance', 'completed')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'is_read')

@admin.register(ScheduledTask)
class ScheduledTaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'supervisor', 'due_date', 'is_completed')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_generated')

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_by', 'upload_date')

