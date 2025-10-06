from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username",
                    "date_of_birth", "is_staff"]

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )


class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'publication_year')
    search_fields = ('title', 'author')
    list_display = ('title', 'author', 'publication_year')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)