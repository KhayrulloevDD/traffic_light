from django.contrib import admin
from .models import User, JuristicPerson, Department


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'phone', 'additional_phone_numbers', 'first_name', 'last_name', 'middle_name',
                    'email', 'is_active', 'type', 'sex', 'timezone', 'vk', 'fb', 'ok', 'instagram',
                    'telegram', 'whats_app', 'viber', 'created_at', 'updated_at']
    ordering = ['id']


@admin.register(JuristicPerson)
class JuristicPersonAdmin(admin.ModelAdmin):
    list_display = ['jurist_id', 'full_name', 'abbreviation', 'inn', 'kpp', 'created_at', 'updated_at']
    ordering = ['id']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'name']
    ordering = ['id']
