book = Book.objects.get(id=1)
book.save()
book.title = 'Nineteen Eighty-Four'

<!-- Book(title='Nineteen Eighty-Four', author='George Orwell', publication_year='1949') -->
