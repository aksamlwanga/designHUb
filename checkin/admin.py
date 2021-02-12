from django.contrib import admin
from .models import Tenant,Temperature
# registering my app in the admin panel
admin.site.register(Tenant)
admin.site.register(Temperature)
