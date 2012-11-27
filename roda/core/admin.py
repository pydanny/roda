from django.contrib import admin

from tastypie.models import ApiKey


class ApiKeyInline(admin.StackedInline):
    model = ApiKey
    extra = 0

# Also.
admin.site.register(ApiKey)
