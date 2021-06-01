from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(car)
admin.site.register(engine)
admin.site.register(spare)
admin.site.register(category)
