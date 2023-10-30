from django.db import models
from users.models import User


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)


class BookIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_date = models.DateField()
    return_date = models.DateField()
    returned = models.BooleanField(default=False)
    reminder_sent = models.BooleanField(default=False)


class BookRequest(models.Model):
    REQUEST_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=REQUEST_STATUS_CHOICES, default='Pending')
    rejection_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} requests {self.book.name}'


class BookReturn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    return_date = models.DateField()

    def __str__(self):
        return f'{self.user} - {self.book}'


class NewBookTicket(models.Model):
    BOOK_TICKET_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, choices=BOOK_TICKET_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f'{self.user} - {self.book_name}'
