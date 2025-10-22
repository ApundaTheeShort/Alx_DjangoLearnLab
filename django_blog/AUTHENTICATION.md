# Authentication System Documentation

This document provides a detailed explanation of the authentication system for the Django blog application.

## 1. Overview

The authentication system is based on Django's built-in authentication framework. It has been customized to use a `CustomUser` model, which allows for additional user profile information to be stored.

## 2. User Model

The `CustomUser` model is defined in `blog/models.py`. It inherits from `django.contrib.auth.models.AbstractUser` and adds the following fields:

-   `first_name`: (CharField) The user's first name.
-   `last_name`: (CharField) The user's last name.
-   `email`: (EmailField) The user's email address. This field is used as the `USERNAME_FIELD`, meaning users log in with their email.
-   `bio`: (TextField) A short biography of the user.
-   `profile_picture`: (ImageField) The user's profile picture.

The `CustomUser` model is managed by a `CustomUserManager`, which provides methods for creating regular users and superusers.

## 3. Authentication Views and URLs

The authentication process is handled by a combination of Django's built-in views and custom views defined in `blog/views.py`. The URL patterns are defined in `blog/urls.py`.

### 3.1. Registration

-   **URL:** `/register/`
-   **View:** `blog.views.register`
-   **Template:** `blog/register.html`
-   **Form:** `blog.forms.UserRegisterForm`

The registration view handles the creation of new user accounts. When a user submits the registration form, the view validates the data and, if valid, saves the new user to the database. After successful registration, the user is redirected to the login page.

**Testing Registration:**

1.  Navigate to `http://127.0.0.1:8000/register/`.
2.  Fill out the registration form with a unique email address and other required information.
3.  Click the "Sign Up" button.
4.  You should be redirected to the login page with a success message.

### 3.2. Login

-   **URL:** `/login/`
-   **View:** `django.contrib.auth.views.LoginView`
-   **Template:** `blog/login.html`

The login view is handled by Django's built-in `LoginView`. It presents a login form to the user and authenticates their credentials. Upon successful login, the user is redirected to the home page.

**Testing Login:**

1.  Navigate to `http://127.0.0.1:8000/login/`.
2.  Enter the email and password of a registered user.
3.  Click the "Login" button.
4.  You should be redirected to the home page and see a "Welcome" message.

### 3.3. Logout

-   **URL:** `/logout/`
-   **View:** `django.contrib.auth.views.LogoutView`
-   **Template:** `blog/logout.html`

The logout view is handled by Django's built-in `LogoutView`. It logs the user out and displays a confirmation message.

**Testing Logout:**

1.  Log in to the application.
2.  Navigate to `http://127.0.0.1:8000/logout/`.
3.  You should be logged out and see a "You have been logged out" message.

### 3.4. Profile

-   **URL:** `/profile/`
-   **View:** `blog.views.profile`
-   **Template:** `blog/profile.html`
-   **Form:** `blog.forms.ProfileUpdateForm`

The profile view allows logged-in users to view and update their profile information. The view is decorated with the `@login_required` decorator, which ensures that only authenticated users can access it.

**Testing Profile:**

1.  Log in to the application.
2.  Navigate to `http://127.0.0.1:8000/profile/`.
3.  You should see your current profile information.
4.  Update your profile information and click the "Update" button.
5.  You should see a success message and the updated information on the page.
