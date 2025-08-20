from django.contrib import admin
from .models import (
    GenderOption, CasteCategory, SpecialCategory, Nationality, BloodGroup, Religion, State,
    StudentBasicInfo, StudentAccount
)

@admin.register(GenderOption, CasteCategory, SpecialCategory, Nationality, BloodGroup, Religion, State)
class LookupAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(StudentBasicInfo)
class StudentBasicInfoAdmin(admin.ModelAdmin):
    list_display = ('student', 'dob', 'caste_category', 'nationality', 'state_of_domicile', 'updated_at')
    search_fields = ('student__first_name', 'student__last_name')
    autocomplete_fields = ('student',)


@admin.register(StudentAccount)
class StudentAccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'mobile')
