class ContactInfo:
    def __init__(self, type: str, value: str):
        if not isinstance(type, str) or not isinstance(value, str):
            raise TypeError('Значения должны быть типа STR')
        self.__type = type
        self.__value = value
    def __str__(self):
        """
        возвращает строку, аккумулирующую состояние всех полей объекта
        """
        return f'Тип контакта:{self.__type}, Значение контакта:{self.__value}'

    def get_type(self) -> str:
        """
        возвращает тип контакта
        """
        return self.__type
    def get_value(self)-> str:
        """
        возвращает значение контакта
        """
        return self.__value

class Genre:
    def __init__(self, name: str, description: str):
        if not isinstance(name, str) or not isinstance(description, str):
            raise TypeError('Значения должны быть типа STR')
        self.__name = name
        self.__description = description
    def __str__(self):
        """
        возвращает строку, аккумулирующую состояние всех полей объекта
        """
        return f'Название жанра:{self.__name}, Описание жанра:{self.__description}'

    def get_name(self) -> str:
        """
        возвращает название жанра
        """
        return self.__name
    def get_description(self) -> str:
        """
        возвращает описание жанра
        """
        return self.__description

class Employee:
    def __init__(self,name: str, position:str, id: int, contacts = None):

        if not isinstance(name, str) or not isinstance(position, str):
            raise TypeError('Имя и должность должны быть типа STR')
        self.__name = name
        self.__position = position

        if not isinstance(id, int):
            raise TypeError('Имя и должность должны быть типа INT')
        self.__id = id

        self.__contacts = contacts or []
    def __str__(self):
        """
        возвращает строку, аккумулирующую состояние всех полей объекта
        """
        return f'Имя:{self.__name}, Должность:{self.__position}, Идентификационный номер:{self.__id}, Контактная информация:{[elem.__str__() for elem in self.__contacts]} '

    def get_name(self) -> str:
        """
        возвращает имя сотрудника
        """
        return self.__name
    def get_position(self) -> str:
        """
        возвращает должность сотрудника
        """
        return self.__position
    def get_id(self) -> int:
        """
        возвращает идентификационный номер сотрудника
        """
        return self.__id
    def get_contact_info(self) -> list[ContactInfo]:
        """
        возвращает контактную информацию сотрудника
        """
        return self.__contacts

    def set_position(self,position: str) -> None:
        """
        устанавливает должность сотрудника
        :param position: новая должность
        :return: None
        """
        self.__position = position
    def add_contact_info(self,contact_info: ContactInfo) -> None:
        """
        добавляет контактную информацию сотрудника
        :param contact_info: контактная информация
        :return: None
        """
        if not isinstance(contact_info, ContactInfo):
            raise TypeError('Контакт должен быть типом ContactInfo')
        elif contact_info in self.__contacts:
            raise ValueError('Контакт уже существует')
        self.__contacts.append(contact_info)
    def remove_contact_info(self,contact_info: ContactInfo) -> None:
        """
        удаляет контактную информацию сотрудника
        :param contact_info: контактная информация
        :return: None
        """
        if not contact_info in self.__contacts:
            raise ValueError('Контакта нет в списке')
        self.__contacts.remove(contact_info)

class Book:
    def __init__(self, title: str, author:str, year: int, id:int, genres = None):
        if not isinstance(title, str) or not isinstance(author, str):
            raise TypeError('Название и автор должны быть типа STR')
        self.__title = title
        self.__author = author

        if not (isinstance(year, int) and len(str(year)) == 4):
            raise TypeError('Год должны быть типа INT и формала <####>')
        self.__year = year

        if not isinstance(id, int):
            raise TypeError('ID должны быть типа INT')
        self.__id = id

        self.__genres = genres or []
    def __str__(self):
        """
        возвращает строку, аккумулирующую состояние всех полей объекта
        """
        return f'Название:{self.__title}, Автора:{self.__author}, Год издания:{self.__year}, Идентификационный номер:{self.__id}, Список жанров:{[elem.__str__() for elem in self.__genres]}'

    def get_title(self) -> str:
        """
        возвращает название книги
        """
        return self.__title
    def get_author(self) -> str:
        """
        возвращает автора книги
        """
        return self.__author
    def get_year(self) -> int:
        """
        возвращает год издания книги
        """
        return self.__year
    def get_id(self) -> int:
        """
        возвращает идентификационный номер книги
        """
        return self.__id
    def get_genres(self) -> list[Genre]:
        """
        возвращает список жанров книги
        """
        return self.__genres

    def set_year(self,year: int) -> None:
        """
        устанавливает год издания книги
        :param year: год издания
        :return: None
        """
        if not (isinstance(year, int) and len(str(year)) == 4):
            raise TypeError('Год должны быть типа INT и формала <####>')
        self.__year = year

    def add_genre(self,genre: Genre) -> None:
        """
        добавляет жанр в список жанров книги
        :param genre: жанр книги
        :return: None
        """
        if not isinstance(genre, Genre):
            raise TypeError('Жанр должен быть типом Genre')
        elif genre in self.__genres:
            raise ValueError('Жанр уже существует')
        self.__genres.append(genre)
    def remove_genre(self,genre: Genre) -> None:
        """
        удаляет жанр из списка жанров книги
        :param genre: жанр книги
        :return: None
        """
        if not genre in self.__genres:
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
        """
        возвращает строку, аккумулирующую состояние всех полей объекта
        """
        return f'Имя:{self.__name},\n Адрес:{self.__address},\n Список книг:{[elem.__str__() for elem in self.__books]},\n Список сотрудников:{[elem.__str__() for elem in self.__employees]}'
    def get_name(self) -> str:
        """
        возвращает имя библиотеки
        """
        return self.__name
    def get_address(self) -> str:
        """
        возвращает адрес библиотеки
        """
        return self.__address
    def get_books(self) -> list[Book]:
        """
        возвращает список книг в библиотеке
        """
        return self.__books
    def get_employees(self) -> list[Employee]:
        """
        возвращает список сотрудников библиотеки
        """
        return self.__employees

    def set_address(self,address: str) -> None:
        """
        устанавливает адрес библиотеки
        :param address: адрес библиотеки
        :return: None
        """
        if not isinstance(address, str):
            raise TypeError('Адрес должны быть типа STR')
        self.__address = address

    def add_book(self,book: Book) -> None:
        """
        добавляет книгу в список книг
        :param book: книга
        :return: None
        """
        if not isinstance(book, Book):
            raise TypeError('Книга должен быть типом Book')
        elif book in self.__books:
            raise ValueError('Книга уже существует')
        self.__books.append(book)
    def remove_book(self,book: Book) -> None:
        """
        удаляет книгу из списка книг
        :param book: книга
        :return: None
        """
        if not book in self.__books:
            raise ValueError('Книги нет в списке')
        self.__books.remove(book)
    def add_employee(self,employee: Employee) -> None:
        """
        добавляет сотрудника в список сотрудников
        :param employee: сотрудник
        :return: None
        """
        if not isinstance(employee, Employee):
            raise TypeError('Сотрудник должен быть типом Employee')
        elif employee in self.__employees:
            raise ValueError('Сотрудник уже существует')
        self.__employees.append(employee)
    def remove_employee(self,employee: Employee) -> None:
        """
        удаляет сотрудника из списка
        :param employee: сотрудник
        :return: None
        """
        if not employee in self.__employees:
            raise ValueError('Сотрудника нет в списке')
        self.__employees.remove(employee)



