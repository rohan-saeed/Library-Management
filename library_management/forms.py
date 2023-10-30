from .models import Book, BookIssue, NewBookTicket
from django import forms


class BookSearchForm(forms.Form):
    q = forms.CharField(label='Search for books', required=False)


class BookReturnForm(forms.Form):
    book_issue = forms.ModelChoiceField(queryset=BookIssue.objects.filter(
        returned=False), label='Select a Book to Return', empty_label='-- Select a Book to Return --')


class BookRequestForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(
    ), label='Select a Book', empty_label='-- Select a Book --')


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = NewBookTicket
        fields = ['user', 'book_name']
