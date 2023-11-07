from django.contrib import admin

from .models import Book, BookIssue, NewBookTicket
# Register your models here.

admin.site.register(Book)
admin.site.register(BookIssue)
admin.site.register(NewBookTicket)
