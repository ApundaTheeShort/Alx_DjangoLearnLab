from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

from .models import Book
# Create your views here.


def index(request): return HttpResponse("Welcome to bookshelf")


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'bookshelf/book_list.html', context)


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}
    return render(request, 'bookshelf/book_details.html', context)


@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return HttpResponse("Book deleted successfully.")

    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
