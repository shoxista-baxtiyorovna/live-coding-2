from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'birth_date', 'nationality']
    search_field = ['first_name', 'last_an']
