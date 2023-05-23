from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

books = [
    {'id': 1, 'title': 'Book 1', 'description': 'Description 1'},
    {'id': 2, 'title': 'Book 2', 'description': 'Description 2'},
    {'id': 3, 'title': 'Book 3', 'description': 'Description 3'},
    {'id': 4, 'title': 'Book 4', 'description': 'Description 4'},
    {'id': 5, 'title': 'Book 5', 'description': 'Description 5'},
    {'id': 6, 'title': 'Book 6', 'description': 'Description 6'},
    {'id': 7, 'title': 'Book 7', 'description': 'Description 7'},
    {'id': 8, 'title': 'Book 8', 'description': 'Description 8'},
    {'id': 9, 'title': 'Book 9', 'description': 'Description 9'},
    {'id': 10, 'title': 'Book 10', 'description': 'Description 10'}
]

def index (request) :
    return render (request , 'book/index.html' , context={'books' : books })


def show (request , bid) :
    my_book = find_book(bid)
    return render (request , 'book/show.html' , context={'book' : my_book })



def create (request):
    return HttpResponse('Hello create')

def edit (request , bid) :

    return render (request , 'book/index.html' , context={'books' : books })



def delete (request , bid) :
    delete_book = find_book(bid)
    del books[delete_book["id"] - 1]
    return render (request , 'book/index.html' , context={'books' : books })


def find_book (bid): 
    for book in books:
        if book["id"] == int(bid):
            return book
