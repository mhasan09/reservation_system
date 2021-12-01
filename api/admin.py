from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(RESERVATION)
class RESERVATION_ADMIN(admin.ModelAdmin):
    list_display = [f.name for f in RESERVATION._meta.fields]
@admin.register(VACANCY)
class VACANCY_ADMIN(admin.ModelAdmin):
    list_display = [f.name for f in VACANCY._meta.fields]
@admin.register(VACANCY_LIMIT)
class VACANCY_LIMIT_ADMIN(admin.ModelAdmin):
    list_display = [f.name for f in VACANCY_LIMIT._meta.fields]