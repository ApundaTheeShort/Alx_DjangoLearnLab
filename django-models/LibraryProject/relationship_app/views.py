from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'home.html')

def list_books(request):
    """
    Function-based view to list all books.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Class-based view to show details of a specific library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('list_books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Add Book'
        return context

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('list_books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Edit Book'
        return context

class BookDelete(DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('list_books')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return BookCreate.as_view()(request)

@permission_required('relationship_app.can_change_book')
def change_book(request, pk):
    return BookUpdate.as_view()(request, pk=pk)

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    return BookDelete.as_view()(request, pk=pk)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

def logout_view(request):
    logout(request)
    return redirect('login')

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

    def get_success_url(self):
        user = self.request.user
        if hasattr(user, 'userprofile'):
            if user.userprofile.role == 'Admin':
                return reverse_lazy('admin_view')
            elif user.userprofile.role == 'Librarian':
                return reverse_lazy('librarian_view')
        return reverse_lazy('member_view')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    
    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Register'
        return context