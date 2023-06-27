from django.contrib import admin
from django.contrib.auth.models import Group, User

from apps.setting.models import Setting

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False