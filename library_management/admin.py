from django.contrib import admin

from .models import Book, BookIssue, BookRequest, BookReturn, NewBookTicket
# Register your models here.

admin.site.register(Book)
admin.site.register(BookIssue)
admin.site.register(BookRequest)
admin.site.register(BookReturn)
admin.site.register(NewBookTicket)
