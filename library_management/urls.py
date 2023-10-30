from django.urls import path
from . import views
urlpatterns = [
    path('', views.BookList.as_view(), name='book-list'),
    path('book_search/<str:book_name>/',
         views.BookSearchView.as_view(), name='book_search_results'),
    path('<int:pk>/', views.BookDetail.as_view()),
    path('issues/', views.BookIssueList.as_view(), name='issues'),
    path('requests/', views.BookRequestList.as_view(), name='requests'),
    path('book_request/', views.BookRequestView.as_view(), name='book_request'),
    path('book_return/', views.BookReturnView.as_view(), name='book_return'),
    path('my_books/', views.MyBooksView.as_view(), name='my_books'),
    path('new_ticket/', views.NewTicketCreateView.as_view(), name='new_ticket'),
    path('my_tickets', views.BookTicketView.as_view(), name='my_tickets'),
    path('dashboard/', views.librarian_dashboard,
         name='librarian_dashboard'),
]
