from library import *

book = Book('1984','Джордж Оруэлл',1949,1)
print('Книга >>>', book)
gen = Genre('Социально-психологическая фантастика','разновидность романа')
print('Жанр >>>', gen)
book.add_genre(gen)
print('В Книгу добавлен Жанр >>>', book)
book.remove_genre(gen)
print('Из Книги удален Жанр >>>', book,'\n')


emp = Employee('Kara','Karatel',1)
print('Cотрудник >>>', emp)
cont = ContactInfo('phone','8-800-555-35-35')
print('Контакт >>>', cont)
emp.add_contact_info(cont)
print('Cотруднику добавлен Контакт >>>', emp)
emp.remove_contact_info(cont)
print('У Cотрудника удален Контакт >>>', emp,'\n')

lib = Library('Gogol','Lenina')
print('Библиотека >>>', lib,'\n')

book.add_genre(gen)
lib.add_book(book)
print('В Библиотеку добалена книга >>>', lib,'\n')

emp.add_contact_info(cont)
lib.add_employee(emp)
print('В Библиотеку добален сотрудник >>>', lib,'\n')

lib.remove_book(book)
print('Из Библиотеки удалена книга >>>', lib,'\n')

lib.remove_employee(emp)
print('Из Библиотеки удален сотрудник >>>', lib,'\n')