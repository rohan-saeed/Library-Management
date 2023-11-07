from django.conf import settings
from django.db import models
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)


class BookIssue(models.Model):
    # REQUEST_STATUS_CHOICES = (
    #     ('Issued', 'Issued'),
    #     ('Pending', 'Pending'),
    #     ('Rejected', 'Rejected'),
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now=True)
    return_date = models.DateField()
    returned = models.BooleanField(default=False)

    class Status(models.TextChoices):
        """
        Status of each request, changed to depict the current status
        Utilized TextChoices here as I required some comparisons with keys using request data
        """
        PENDING = "pending", "Pending"
        ISSUED = "issued", "Issued"
        REJECTED = "rejected", "Rejected"
    status = models.CharField(choices=Status.choices,
                              max_length=9, default=Status.PENDING)

    # status = models.CharField(
    #     max_length=20, choices=REQUEST_STATUS_CHOICES, default='Pending')


class NewBookTicket(models.Model):
    BOOK_TICKET_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=BOOK_TICKET_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f'{self.user} - {self.book}'


@receiver(post_save, sender=NewBookTicket)
def call_car_api(sender, instance, **kwargs):
    subject = 'Ticket Received'
    message = f"Dear {instance.user.username}, we have got your request regarding '{instance.book.name}'. We will soon inform you about availability ."
    from_email = 'rohan.saeed@arbisoft.com'
    recipient_list = [instance.user.email]

    send_mail(subject, message, from_email,
              recipient_list, fail_silently=False)

    print('Ticket object created')
    print(sender, instance, kwargs)
