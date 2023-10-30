from .models import BookRequest
from .forms import NewTicketForm
from .models import BookIssue, BookRequest, BookReturn, NewBookTicket
from .forms import BookReturnForm
from .models import BookIssue
from .forms import BookRequestForm
from django.shortcuts import render, redirect
from django.views import View
from .models import Book
from django.views.generic import ListView
from django.shortcuts import render
from .permissions import IsStaffEditorPermission
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import NewBookTicket
from .forms import NewTicketForm
from rest_framework import generics
from .models import Book, BookIssue, BookRequest
from .serializers import BookSerializer, BookIssueSerializer, BookRequestSerializer, BookTicketSerializer
from django.utils import timezone
from django.http import HttpResponse


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStaffEditorPermission]


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookIssueList(generics.ListCreateAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer


class BookRequestList (generics.ListAPIView):
    queryset = BookRequest.objects.all()
    serializer_class = BookRequestSerializer


class BookSearchView(View):
    template_name = 'book_search_results.html'

    def get(self, request, *args, **kwargs):
        book_name = self.kwargs['book_name']
        books = Book.objects.filter(name__icontains=book_name)
        return render(request, 'book_search_results.html', {'books': books, 'book_name': book_name})


class BookRequestView(View):
    template_name = 'book_request.html'

    def get(self, request):
        form = BookRequestForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BookRequestForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            max_requests = 3
            user_requests = BookRequest.objects.filter(
                user=request.user, status='Pending').count()

            if user_requests >= max_requests:
                return render(request, 'max_requests.html')
            BookRequest.objects.create(user=request.user, book=book)
            return redirect('requests')

        return render(request, self.template_name, {'form': form})


class BookReturnView(View):
    template_name = 'book_return.html'

    def get(self, request):
        books_issued = BookIssue.objects.filter(
            user=request.user, returned=False)
        form = BookReturnForm()
        return render(request, self.template_name, {'books_issued': books_issued, 'form': form})

    def post(self, request):
        form = BookReturnForm(request.POST)
        if form.is_valid():

            book_issue_id = form.cleaned_data['book_issue_id']
            book_issue = BookIssue.objects.get(id=book_issue_id)

            book_issue.returned = True

            book_issue.return_date = timezone.now()

            book_issue.save()

            return redirect('issues')

        books_issued = BookIssue.objects.filter(
            user=request.user, returned=False)
        return render(request, self.template_name, {'books_issued': books_issued, 'form': form})


class MyBooksView(ListView):
    template_name = 'my_books.html'
    context_object_name = 'my_books'

    def get_queryset(self):
        user = self.request.user
        issued_books = BookIssue.objects.filter(user=user, returned=False)
        requested_books = BookRequest.objects.filter(user=user)
        returned_books = BookReturn.objects.filter(user=user)

        return {
            'issued_books': issued_books,
            'requested_books': requested_books,
            'returned_books': returned_books,
        }


class NewTicketCreateView(CreateView):
    model = NewBookTicket
    form_class = NewTicketForm
    template_name = 'new_ticket.html'
    success_url = reverse_lazy('my_tickets')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookTicketView(generics.ListAPIView):
    queryset = NewBookTicket.objects.all()
    serializer_class = BookTicketSerializer


def librarian_dashboard(request):
    pending_requests = BookRequest.objects.filter(status='Pending')
    return render(request, 'librarian_dashboard.html', {'pending_requests': pending_requests})


def accept_request(request, request_id):
    book_request = BookRequest.objects.get(pk=request_id)
    if book_request.status == 'pending':
        book_request.save(status='accepted')

        return redirect('librarian_dashboard')

    return HttpResponse('Invalid request')


def reject_request(request, request_id):
    book_request = BookRequest.objects.get(pk=request_id)
    if book_request.status == 'pending':
        book_request.status = 'rejected'
        rejection_reason = request.POST.get('rejection_reason')
        book_request.rejection_reason = rejection_reason
        book_request.save()
        return redirect('librarian_dashboard')

    return HttpResponse('Invalid request')
