from django.contrib import admin

from .models import (
    Department,
    Student
)


# =====================================================
# DEPARTMENT ADMIN
# =====================================================

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'english_name',
        'hindi_name',
    )

    search_fields = (
        'english_name',
        'hindi_name',
    )

    ordering = (
        'english_name',
    )

    list_per_page = 25


# =====================================================
# STUDENT ADMIN
# =====================================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # -------------------------------------------------
    # TABLE COLUMNS
    # -------------------------------------------------

    list_display = (
        'english_name',
        'registration_no',
        'degree',
        'department',
        'cgpa',
        'completion_year',
    )

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    search_fields = (
        'english_name',
        'hindi_name',
        'registration_no',
        'enrollment_no',
    )

    # -------------------------------------------------
    # FILTERS
    # -------------------------------------------------

    list_filter = (
        'degree',
        'department',
        'completion_month',
        'completion_year',
    )

    # -------------------------------------------------
    # SORTING
    # -------------------------------------------------

    ordering = (
        '-completion_year',
        'english_name',
    )

    # -------------------------------------------------
    # READ ONLY
    # -------------------------------------------------

    readonly_fields = (
        'created_at',
    )

    # -------------------------------------------------
    # ADMIN FORM GROUPING
    # -------------------------------------------------

    fieldsets = (

        (
            'Student Information',
            {
                'fields': (
                    'english_name',
                    'hindi_name',
                    'student_photo',
                ),

                'description':
                    'Enter student names and upload photo.'
            }
        ),

        (
            'Registration Details',
            {
                'fields': (
                    'registration_no',
                    'enrollment_no',
                ),

                'description':
                    'Unique registration and enrollment details.'
            }
        ),

        (
            'Academic Information',
            {
                'fields': (
                    'degree',
                    'department',
                    'cgpa',
                ),

                'description':
                    'Select degree and department from dropdown.'
            }
        ),

        (
            'Course Completion',
            {
                'fields': (
                    'completion_month',
                    'completion_year',
                ),

                'description':
                    'Select completion month and year.'
            }
        ),

        (
            'Award Information',
            {
                'fields': (
                    'award_date',
                ),

                'description':
                    'Choose official degree award date.'
            }
        ),

        (
            'System Information',
            {
                'fields': (
                    'created_at',
                ),
            }
        ),
    )

    # -------------------------------------------------
    # PAGINATION
    # -------------------------------------------------

    list_per_page = 20