from django.contrib import admin
from .models import Aircraft
# Register your models here.
# admin.site.register(Aircraft)

@admin.register(Aircraft)
class ItemAdmin(admin.ModelAdmin):
    # exclude=("fueltank_cap_liters", "consumpt_per_minute_liters","max_minutes")
    readonly_fields=("fueltank_cap_liters", "consumpt_per_minute_liters","max_minutes")