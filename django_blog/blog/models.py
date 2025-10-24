from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extrafields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)

        if extrafields.get('is_staff') is not True:
            raise ValueError("Superuser must be is_staff")
        if extrafields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be set to True')

        return self.create_user(email, password, **extrafields)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics', blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.email} on {self.post.title}'
