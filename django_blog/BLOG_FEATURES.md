# Blog Post Features Documentation

This document outlines the features related to blog post management within the application.

## 1. Post Creation

**URL:** `/post/new/`

**Method:** `GET` (to display the form), `POST` (to submit the form)

**Permissions:** Only authenticated (logged-in) users can create new blog posts.

**Usage:**
To create a new blog post, navigate to the `/post/new/` URL. A form will be displayed allowing the user to enter the post's title and content. Upon successful submission, the post will be created, and the user will be redirected to the detail page of the newly created post.

**Data Handling:**
*   **Title:** Required, maximum 200 characters.
*   **Content:** Required, free-form text.
*   **Author:** Automatically set to the currently logged-in user. This field is not exposed in the form.
*   **Published Date:** Automatically set to the current timestamp upon creation.

## 2. Post Updating

**URL:** `/post/<int:pk>/update/`

**Method:** `GET` (to display the form with existing data), `POST` (to submit the updated form)

**Permissions:** Only authenticated users who are the *author* of the post can update it.

**Usage:**
To update an existing blog post, navigate to the `/post/<post_id>/update/` URL, replacing `<post_id>` with the primary key (ID) of the post you wish to edit. The form will pre-populate with the post's current title and content. Upon successful submission, the post will be updated, and the user will be redirected to the post's detail page.

**Data Handling:**
*   **Title:** Can be modified.
*   **Content:** Can be modified.
*   **Author:** Remains the original author and cannot be changed via this form.

## 3. Post Viewing (Detail)

**URL:** `/post/<int:pk>/`

**Method:** `GET`

**Permissions:** All users (authenticated or unauthenticated) can view individual blog posts.

**Usage:**
To view a specific blog post, navigate to the `/post/<post_id>/` URL, replacing `<post_id>` with the primary key (ID) of the post. This page displays the post's title, content, author, and published date.

## 4. Form Validation

All forms used for post creation and updating (`PostForm`) include built-in Django model form validation, ensuring that required fields are present and data types are correct according to the `Post` model definition.
