from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (-('Personal Info'), {'fields': ('name',)}),
        (
            _('Permisions'),
            {'fields': ('is_actice', 'is_superuser')}
        ),
        (_('Importand Dates'), {'fields': ('last_login',)})
    )


admin.site.register(models.User, UserAdmin)
