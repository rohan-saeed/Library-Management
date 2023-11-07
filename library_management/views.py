from .models import Book, BookIssue, NewBookTicket
from .permissions import IsStaffEditorPermission
from rest_framework import generics
from .serializers import BookSerializer, UserIssueSerializer,  LibrarianIssueSerializer, LibrarianUpdateIssueSerializer, UserTicketSerializer, LibrarianTicketSerializer, LibrarianUpdateTicketSerializer, UserUpdateIssueSerializer, UserUpdateTicketSerializer


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
        if not self.request.user.is_librarian:
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
        return UserUpdateIssueSerializer


class BookTicketView(generics.ListCreateAPIView):
    queryset = NewBookTicket.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_librarian:
            return LibrarianTicketSerializer
        return UserTicketSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_librarian:
            queryset = queryset.filter(user=self.request.user)
        return queryset


class BookTicketDetail(generics.RetrieveUpdateAPIView):
    queryset = NewBookTicket.objects.all()
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.user.is_librarian:
            return LibrarianUpdateTicketSerializer
        return UserUpdateTicketSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
