# myapp/management/commands/import_books_from_csv.py
import csv
from django.core.management.base import BaseCommand

from library_management.models import Book


class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    title = row['title']
                    author = row['author']
                    publisher = row['publisher']
                    available_quantity = int(row['available_quantity'])

                    book, created = Book.objects.get_or_create(
                        name=title,
                        author=author,
                        publisher=publisher,
                        defaults={'quantity': available_quantity}
                    )

                    if not created:
                        book.quantity = available_quantity
                        book.save()

                    self.stdout.write(self.style.SUCCESS(
                        f'Successfully imported book: {title}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(
                'File not found. Please check the file path.'))
