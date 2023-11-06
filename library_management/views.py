from .models import Book, BookIssue, NewBookTicket
from .permissions import IsStaffEditorPermission
from rest_framework import generics
from .serializers import BookSerializer, UserIssueSerializer,  LibrarianIssueSerializer, LibrarianUpdateIssueSerializer, UserTicketSerializer, LibrarianTicketSerializer, LibrarianUpdateTicketSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStaffEditorPermission]

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        return queryset


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookIssueList(generics.ListCreateAPIView):
    queryset = BookIssue.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.request.user.is_librarian:
            return LibrarianIssueSerializer
        return UserIssueSerializer


class BookIssueDetail(generics.RetrieveUpdateAPIView):
    queryset = BookIssue.objects.all()
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.user.is_librarian:
            return LibrarianUpdateIssueSerializer
        return UserIssueSerializer


# class BookRequestView(View):
#     template_name = 'book_request.html'

#     def get(self, request):
#         form = BookRequestForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = BookRequestForm(request.POST)
#         if form.is_valid():
#             book = form.cleaned_data['book']
#             max_requests = 3
#             user_requests = BookRequest.objects.filter(
#                 user=request.user, status='Pending').count()

#             if user_requests >= max_requests:
#                 return render(request, 'max_requests.html')
#             BookRequest.objects.create(user=request.user, book=book)
#             return redirect('requests')

#         return render(request, self.template_name, {'form': form})


class BookTicketView(generics.ListCreateAPIView):
    queryset = NewBookTicket.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_librarian:
            return LibrarianTicketSerializer
        return UserTicketSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class BookTicketDetail(generics.RetrieveUpdateAPIView):
    queryset = BookIssue.objects.all()
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.user.is_librarian:
            return LibrarianUpdateTicketSerializer
        return UserTicketSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
