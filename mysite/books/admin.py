from django.contrib import admin

# Register your models here.

from books.models import Publisher, Author, Book

admin.site.register(Publisher)
# admin.site.register(Author)
# admin.site.register(Book)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    # fields = ('title', 'authors', 'publisher')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)