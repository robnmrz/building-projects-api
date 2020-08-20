from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _ # --> converts srings to human readable text to pass it thorugh the django translation engine (recommended convention)

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id'] # orders by id
    list_display = ['email', 'name', 'is_staff']
    fieldsets = (
        # defining / chaning default fields of "change user page" for Users in admin area
        (None, {'fields': ('email', 'password')}), # None = title for section, defining the fields as email and password instead of username and password
        (_('Personal Info'), {'fields': ('name',)}), 
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        # customizing the "add user page" in admin area to only take email, password/password2 
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2',)
        }), 
    )

admin.site.register(models.User, UserAdmin)