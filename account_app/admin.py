import csv

from django.http import HttpResponse

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Account


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta  # noqa
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, delimiter=';')

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = 'Экспортировать в CSV'


@admin.register(Account)
class AccountAdmin(UserAdmin, ExportCsvMixin):

    list_display = ['email', 'is_admin', 'is_active', 'date_joined']
    list_filter = ['is_admin', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('Personal info', {'fields': ('password',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser')}),

    )
    search_fields = ['email',]
    ordering = ['date_joined',]
    actions = ["export_as_csv"]

    filter_horizontal = ()



admin.site.unregister(Group)