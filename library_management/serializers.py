from rest_framework import serializers
from .models import Book, BookIssue, BookRequest, NewBookTicket


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = '__all__'


class BookRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRequest
        fields = '__all__'


class BookTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBookTicket
        fields = '__all__'
