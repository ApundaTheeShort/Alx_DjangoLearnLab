from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Librarian)
admin.site.register(models.Library)
admin.site.register(models.UserProfile)

# class LibraryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'books')
#     search_fields = ('name', 'books__title')

# admin.site.register(models.Library, LibraryAdmin)