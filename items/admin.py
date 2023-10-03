from django.contrib import admin
from .models import category
from .models import items

admin.site.register(category)
admin.site.register(items)

