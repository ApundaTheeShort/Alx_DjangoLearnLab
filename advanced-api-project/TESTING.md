# Testing Strategy

This document outlines the testing strategy for the advanced API project, including how to run tests and interpret their results.

## Testing Framework

The project uses Django's built-in testing framework, which is based on Python's `unittest` module. Tests are written as classes that inherit from `django.test.TestCase`.

## Test Scenarios

The testing strategy focuses on ensuring the reliability and security of the API by covering the following scenarios:

- **Authentication and Authorization**: Tests verify that protected endpoints require authentication and that users can only access resources they are permitted to.
- **CRUD Operations**: Tests cover the Create, Read, Update, and Delete operations for each model to ensure they function as expected.
- **Validation**: Tests check that the API correctly handles both valid and invalid data, returning appropriate error messages when validation fails.
- **Filtering, Searching, and Ordering**: Tests verify that the API correctly filters, searches, and orders results based on query parameters.

## Individual Test Cases

The following test cases are implemented in `api/test_views.py`:

- **`test_book_list_unauthenticated`**: Verifies that unauthenticated users can retrieve a list of all books.
- **`test_book_detail_unauthenticated`**: Ensures that unauthenticated users can retrieve a single book by its ID.
- **`test_create_book_authenticated`**: Confirms that authenticated users can create a new book.
- **`test_create_book_unauthenticated`**: Checks that unauthenticated users are forbidden from creating a new book.
- **`test_update_book_authenticated`**: Verifies that authenticated users can update an existing book.
- **`test_update_book_unauthenticated`**: Ensures that unauthenticated users are forbidden from updating a book.
- **`test_delete_book_authenticated`**: Confirms that authenticated users can delete a book.
- **`test_delete_book_unauthenticated`**: Checks that unauthenticated users are forbidden from deleting a book.
- **`test_filter_by_publication_year`**: Verifies that the API can filter books by publication year.
- **`test_search_by_title`**: Ensures that the API can search for books by title.
- **`test_order_by_title`**: Confirms that the API can order books by title.

## Running Tests

To run the tests, follow these steps:

1. **Activate the virtual environment**:

   ```bash
   source env/bin/activate
   ```

2. **Run the tests**:

   ```bash
   python manage.py test api
   ```

## Interpreting Test Results

When you run the tests, you will see output indicating the status of each test case:

- **`.` (dot)**: Indicates that the test passed successfully.
- **`E`**: Indicates that an error occurred during the test.
- **`F`**: Indicates that the test failed (i.e., an assertion was not met).

If all tests pass, you will see an **`OK`** message at the end. If any tests fail or produce errors, a summary of the failures and errors will be displayed, along with a traceback to help you identify the cause of the issue.