from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Grade, Feedback

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'student_id', 'name', 'age', 'email')
    search_fields = ('name', 'student_id', 'email')
    list_filter = ('age',)
    ordering = ('student_id',)

    def thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 30px; height: 30px; border-radius: 50%;" />', obj.photo.url)
        return "No Image"
    thumbnail.short_description = 'Photo'

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade')
    list_filter = ('subject', 'student')
    search_fields = ('student__name', 'subject')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'submitted_at', 'comment_excerpt')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)

    def comment_excerpt(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment