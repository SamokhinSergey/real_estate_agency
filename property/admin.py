from django.contrib import admin
from .models import Flat
from .models import Complaint
from .models import Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = (
        'owner',
        'flat',
    )


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerInline]
    search_fields = (
        'town',
        'address',
        'owner'
    )
    readonly_fields = (
        "created_at",
    )
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    list_editable = (
        'new_building',
    )

    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
    )
    raw_id_fields = (
        'liked_by',
    )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'user',
        'flat',
    )


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'flats',
    )

