class ContactInfo:


    def __init__(self, type: str, value: str):

        if not isinstance(type, str) or not isinstance(value, str):
            raise TypeError('Значения должны быть типа STR')

        self.__type = type
        self.__value = value

    def __str__(self):
        return f'Тип контакта:{self.__type}, Значение контакта:{self.__value}'

    def get_type(self) -> str:
        return self.__type

    def get_value(self) -> str:
        return self.__value


class Genre:


    def __init__(self, name: str, description: str):

        if not isinstance(name, str) or not isinstance(description, str):
            raise TypeError('Значения должны быть типа STR')

        self.__name = name
        self.__description = description

    def __str__(self):
        return f'Название жанра:{self.__name}, Описание жанра:{self.__description}'

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description


class Employee:


    def __init__(self,name: str, position:str, id: int, contacts = None):

        if not isinstance(name, str) or not isinstance(position, str):
            raise TypeError('Имя и должность должны быть типа STR')

        if not isinstance(id, int):
            raise TypeError('Имя и должность должны быть типа INT')

        self.__name = name
        self.__position = position
        self.__id = id
        self.__contacts = contacts or []

    def __str__(self):
        return f'Имя:{self.__name}, Должность:{self.__position}, Идентификационный номер:{self.__id}, Контактная информация:{[elem.__str__() for elem in self.__contacts]} '

    def get_name(self) -> str:
        return self.__name

    def get_position(self) -> str:
        return self.__position

    def get_id(self) -> int:
        return self.__id

    def get_contact_info(self) -> list[ContactInfo]:
        return self.__contacts

    def set_position(self,position: str) -> None:
        self.__position = position

    def in_contacts(self,contact_info: ContactInfo) -> bool:

        if not isinstance(contact_info, ContactInfo):
            raise TypeError('Контакт должен быть типом ContactInfo')

        return contact_info in self.__contacts

    def add_contact_info(self,contact_info: ContactInfo) -> None:

        if self.in_contacts(contact_info):
            raise ValueError('Контакт уже существует')

        self.__contacts.append(contact_info)

    def remove_contact_info(self,contact_info: ContactInfo) -> None:

        if not self.in_contacts(contact_info):
            raise ValueError('Контакта нет в списке')

        self.__contacts.remove(contact_info)


class Book:


    def __init__(self, title: str, author:str, year: int, id:int, genres = None):

        if not isinstance(title, str) or not isinstance(author, str):
            raise TypeError('Название и автор должны быть типа STR')

        if not (isinstance(year, int) and len(str(year)) == 4):
            raise TypeError('Год должны быть типа INT и формала <####>')

        if not isinstance(id, int):
            raise TypeError('ID должны быть типа INT')

        self.__title = title
        self.__author = author
        self.__year = year
        self.__id = id
        self.__genres = genres or []

    def __str__(self):
        return f'Название:{self.__title}, Автора:{self.__author}, Год издания:{self.__year}, Идентификационный номер:{self.__id}, Список жанров:{[elem.__str__() for elem in self.__genres]}'

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_year(self) -> int:
        return self.__year

    def get_id(self) -> int:
        return self.__id

    def get_genres(self) -> list[Genre]:
        return self.__genres

    def set_year(self,year: int) -> None:

        if not (isinstance(year, int) and len(str(year)) == 4):
            raise TypeError('Год должны быть типа INT и формала <####>')

        self.__year = year

    def in_genres(self,genre: Genre) -> bool:

        if not isinstance(genre, Genre):
            raise TypeError('Жанр должен быть типом Genre')

        return genre in self.__genres

    def add_genre(self,genre: Genre) -> None:

        if self.in_genres(genre):
            raise ValueError('Жанр уже существует')

        self.__genres.append(genre)

    def remove_genre(self,genre: Genre) -> None:

        if not self.in_genres(genre):
            raise ValueError('Жанра нет в списке')

        self.__genres.remove(genre)


class Library:


    def __init__(self, name: str, address: str, books = None, employees = None):

        if not isinstance(name, str) or not isinstance(address, str):
            raise TypeError('Имя и адрес должны быть типа STR')

        self.__name = name
        self.__address = address
        self.__books = books or []
        self.__employees = employees or []

    def __str__(self):
        return f'Имя:{self.__name},\n Адрес:{self.__address},\n Список книг:{[elem.__str__() for elem in self.__books]},\n Список сотрудников:{[elem.__str__() for elem in self.__employees]}'

    def get_name(self) -> str:
        return self.__name

    def get_address(self) -> str:
        return self.__address

    def get_books(self) -> list[Book]:
        return self.__books

    def get_employees(self) -> list[Employee]:
        return self.__employees

    def set_address(self,address: str) -> None:

        if not isinstance(address, str):
            raise TypeError('Адрес должны быть типа STR')

        self.__address = address

    def in_books(self,book: Book) -> bool:
        if not isinstance(book, Book):
            raise TypeError('Книга должен быть типом Book')

        return book in self.__books

    def add_book(self,book: Book) -> None:

        if self.in_books(book):
            raise ValueError('Книга уже существует')

        self.__books.append(book)

    def remove_book(self,book: Book) -> None:

        if not self.in_books(book):
            raise ValueError('Книги нет в списке')

        self.__books.remove(book)

    def in_employees(self, employee: Employee) -> bool:

        if not isinstance(employee, Employee):
            raise TypeError('Сотрудник должен быть типом Employee')

        return employee in self.__employees

    def add_employee(self,employee: Employee) -> None:

        if self.in_employees(employee):
            raise ValueError('Сотрудник уже существует')

        self.__employees.append(employee)

    def remove_employee(self,employee: Employee) -> None:

        if not self.in_employees(employee):
            raise ValueError('Сотрудника нет в списке')

        self.__employees.remove(employee)



