from django.urls import path
from . import views
urlpatterns = [

    path('', views.BookList.as_view(), name='book-list'),
    path('<int:pk>/', views.BookDetail.as_view()),

    path('issues/', views.BookIssueList.as_view(), name='issues'),
    path('issues/<int:pk>/', views.BookIssueDetail.as_view()),

    path('tickets/', views.BookTicketView.as_view(), name='tickets'),
    path('tickets/<int:pk>/', views.BookTicketDetail.as_view()),
]
