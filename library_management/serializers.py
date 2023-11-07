from rest_framework import serializers
from .models import Book, BookIssue, NewBookTicket


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publisher', 'image', 'quantity']


class UserIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = ['user', 'book',
                  'issued_date', 'returned', 'return_date']
        read_only_fields = ['returned']
        extra_kwargs = {'user': {'default': serializers.CurrentUserDefault()}}


class LibrarianIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = ['user', 'book', 'issued_date',
                  'returned', 'return_date', 'status']


class LibrarianUpdateIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = ['user', 'book', 'issued_date',
                  'returned', 'return_date', 'status']
        read_only_fields = ['id', 'user', 'book']


class UserUpdateIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = ['user', 'book',
                  'issued_date', 'returned', 'return_date']
        read_only_fields = fields


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
        model = NewBookTicket
        fields = ['id', 'user', 'book', 'status']
        read_only_fields = ['id', 'user', 'book']


class UserUpdateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBookTicket
        fields = ['id', 'user', 'book', 'status']
        read_only_fields = fields
