from django.contrib import admin
from .models import Click, Scroll, TimeSpent

admin.site.register(Click)
admin.site.register(Scroll)
admin.site.register(TimeSpent)
