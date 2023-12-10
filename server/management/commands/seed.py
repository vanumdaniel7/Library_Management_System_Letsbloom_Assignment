from random import choice
from server.models import Book
from server.serializers import BookSerializer
from django.core.management.base import BaseCommand
# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type = str, help = "Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

def clear_data():
    """Deletes all the table data"""
    Book.objects.all().delete()


def create_address():
    """Creates an address object combining different elements from the list"""
    titles = [
        "The Catcher in the Rye",
        "To Kill a Mockingbird",
        "1984",
        "The Great Gatsby",
        "Moby-Dick",
        "Pride and Prejudice",
        "The Hobbit",
        "One Hundred Years of Solitude",
        "The Lord of the Rings",
        "Harry Potter and the Sorcerer's Stone",
        "The Da Vinci Code",
        "The Hitchhiker's Guide to the Galaxy",
        "Brave New World",
        "The Shining",
        "The Hunger Games",
        "The Chronicles of Narnia",
        "The Alchemist",
        "The Girl with the Dragon Tattoo",
        "A Song of Ice and Fire",
        "Sapiens: A Brief History of Humankind"
    ]
    authors = [
        "J.D. Salinger",
        "Harper Lee",
        "George Orwell",
        "F. Scott Fitzgerald",
        "Herman Melville",
        "Jane Austen",
        "J.R.R. Tolkien",
        "Gabriel Garcia Marquez",
        "J.K. Rowling",
        "Dan Brown",
        "Douglas Adams",
        "Aldous Huxley",
        "Stephen King",
        "Suzanne Collins",
        "C.S. Lewis",
        "Paulo Coelho",
        "Stieg Larsson",
        "George R.R. Martin",
        "Yuval Noah Harari"
    ]
    editions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    publishers = [
        "Springer",
        "Elsevier",
        "IEEE (Institute of Electrical and Electronics Engineers)",
        "ACM (Association for Computing Machinery)",
        "O'Reilly Media",
        "Wiley",
        "Taylor & Francis",
        "Pearson",
        "MIT Press",
        "Cambridge University Press"
    ]
    languages = [
        "English",
        "Spanish",
        "French",
        "German",
        "Mandarin Chinese",
        "Arabic",
        "Russian",
        "Hindi",
        "Portuguese",
        "Japanese",
        "Italian",
        "Korean",
        "Dutch",
        "Swedish",
        "Turkish",
        "Hebrew",
        "Vietnamese",
        "Greek",
        "Polish",
        "Thai",
        "Farsi (Persian)",
        "Bengali",
        "Urdu",
        "Swahili",
        "Tagalog",
    ]
    publicationDates = [
        '2022-01-15', 
        '2022-02-28', 
        '2022-03-12', 
        '2022-04-04', 
        '2022-05-20', 
        '2022-06-08', 
        '2022-07-17', 
        '2022-08-22', 
        '2022-09-09', 
        '2022-10-11', 
        '2022-11-05', 
        '2022-12-30'
    ]
    numberOfCopies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    serializer = BookSerializer(data = {
        "title": choice(titles),
        "author": choice(authors),
        "edition": choice(editions),
        "publisher": choice(publishers),
        "language": choice(languages),
        "publicationDate": choice(publicationDates),
        "numberOfCopies": choice(numberOfCopies)
    })

    if serializer.is_valid():
        serializer.save()

    return serializer

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 addresses
    for i in range(30):
        create_address()