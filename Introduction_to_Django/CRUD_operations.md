<!-- CREATE -->

> > > new_book = Book(title='1984', author='George Orwell', publication_year='1949')
> > > new_book.save()

<!-- OUTPUT -->

Book(title='1984', author='George Orwell', publication_year='1949')

<!-- UPDATE -->

> > > book = Book.objects.get(id=1)
> > > book.title = 'Nineteen Eighty-Four'
> > > book.save()

<!-- OUTPUT -->

Book(title='Nineteen Eighty-Four', author='George Orwell', publication_year='1949')

<!-- DELETE -->

> > > book = Book.objects.get(id=1)
> > > book.delete()

<!-- OUTPUT -->

<QuerySet []>
