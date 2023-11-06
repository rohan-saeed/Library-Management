from rest_framework import serializers
from .models import Book, BookIssue, NewBookTicket


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publisher', 'image', 'quantity']


class UserIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = ['id', 'user', 'book',
                  'issued_date', 'returned', 'return_date']


class LibrarianIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = ['id', 'user', 'book', 'issued_date',
                  'returned', 'return_date', 'status']
        read_only_fields = fields


class LibrarianUpdateIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = ['id', 'user', 'book', 'issued_date',
                  'returned', 'return_date', 'status']
        read_only_fields = ['id', 'user', 'book']


class UserTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBookTicket
        fields = ['id', 'user', 'book', 'status']
        read_only_fields = ['status']


class LibrarianTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBookTicket
        fields = ['id', 'user', 'book', 'status']
        read_only_fields = fields


class LibrarianUpdateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = ['id', 'user', 'book', 'status']
        read_only_fields = ['id', 'user', 'book']
