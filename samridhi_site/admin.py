from django.contrib import admin
from .models import Baseline, Enrollment, Academics, Health

admin.site.register(Baseline)
admin.site.register(Enrollment)
admin.site.register(Academics)
admin.site.register(Health)
