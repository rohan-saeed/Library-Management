from django.core.mail import send_mail
from django.utils import timezone
from .models import BookIssue, Book


def send_return_reminders():
    actual_return_date = timezone.now() - timezone.timedelta(days=15)
    overdue_books = BookIssue.objects.filter(
        return_date__lt=actual_return_date, is_returned=False)

    for book in overdue_books:
        user = book.user
        subject = 'Return Reminder'
        message = f"Dear {user.username}, please remember to return the book '{book.book.name}' as soon as possible."
        from_email = 'rohan.saeed@arbisoft.com'
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)
