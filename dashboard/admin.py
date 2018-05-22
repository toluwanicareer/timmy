from django.contrib import admin
from .models import Match, Plan, Evidence, Investment, Payment

# Register your models here.
admin.site.register(Plan)
admin.site.register(Match)
admin.site.register(Evidence)
admin.site.register(Investment)
admin.site.register(Payment)