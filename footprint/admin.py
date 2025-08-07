from django.contrib import admin
from .models import (
    Household, EnergyUsage, Transportation, Diet, Waste, 
    CarbonFootprint, SustainabilityTip
)


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'family_size', 'user', 'created_at')
    list_filter = ('state', 'family_size', 'created_at')
    search_fields = ('name', 'city', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(EnergyUsage)
class EnergyUsageAdmin(admin.ModelAdmin):
    list_display = ('household', 'fuel_type', 'consumption', 'unit', 'month', 'created_at')
    list_filter = ('fuel_type', 'unit', 'month', 'created_at')
    search_fields = ('household__name', 'household__user__username')
    readonly_fields = ('created_at',)
    ordering = ('-month', '-created_at')


@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ('household', 'vehicle_type', 'distance_km', 'frequency_per_week', 'month', 'created_at')
    list_filter = ('vehicle_type', 'month', 'created_at')
    search_fields = ('household__name', 'household__user__username')
    readonly_fields = ('created_at',)
    ordering = ('-month', '-created_at')


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display = ('household', 'food_type', 'consumption_kg', 'month', 'created_at')
    list_filter = ('food_type', 'month', 'created_at')
    search_fields = ('household__name', 'household__user__username')
    readonly_fields = ('created_at',)
    ordering = ('-month', '-created_at')


@admin.register(Waste)
class WasteAdmin(admin.ModelAdmin):
    list_display = ('household', 'waste_type', 'quantity_kg', 'month', 'created_at')
    list_filter = ('waste_type', 'month', 'created_at')
    search_fields = ('household__name', 'household__user__username')
    readonly_fields = ('created_at',)
    ordering = ('-month', '-created_at')


@admin.register(CarbonFootprint)
class CarbonFootprintAdmin(admin.ModelAdmin):
    list_display = ('household', 'total_footprint', 'energy_footprint', 'transport_footprint', 'diet_footprint', 'waste_footprint', 'month', 'created_at')
    list_filter = ('month', 'created_at')
    search_fields = ('household__name', 'household__user__username')
    readonly_fields = ('created_at',)
    ordering = ('-month', '-created_at')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('household', 'household__user')


@admin.register(SustainabilityTip)
class SustainabilityTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'impact_kg_co2', 'indian_context', 'created_at')
    list_filter = ('category', 'indian_context', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Impact & Context', {
            'fields': ('impact_kg_co2', 'indian_context')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    ) 