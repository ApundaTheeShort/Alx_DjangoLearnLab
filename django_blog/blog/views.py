from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import generics, viewsets
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .forms import UserRegisterForm, ProfileUpdateForm, PostForm, CommentForm
from .models import Post, CustomUser, Comment
from .serializers import PostSerializer, CustomUserSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from taggit.models import Tag

def tagged(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/tagged.html', {'posts': posts, 'tag': tag})

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})


def home(request):
    posts = Post.objects.order_by('-published_date')[:5]
    return render(request, 'blog/home.html', {'posts': posts})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'blog/profile.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all().order_by('-created_at')
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'  # We will render on the post detail page

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs.get('pk')})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        comment = self.get_object()
        return reverse('post-detail', kwargs={'pk': comment.post.pk})

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class ListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class CreateView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
