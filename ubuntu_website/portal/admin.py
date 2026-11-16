from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ServiceRequest, Opportunity, Application

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (('Role', {'fields': ('role',)}),)
    add_fieldsets = BaseUserAdmin.add_fieldsets + (('Role', {'fields': ('role',)}),)

admin.site.register(User, UserAdmin)
admin.site.register(ServiceRequest)
admin.site.register(Opportunity)
admin.site.register(Application)

# Register your models here.
