from django.contrib import admin

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'publication_year')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)
