class Student:
    def __init__(self, first_name: str, second_name: str, age: int, average_score: int or float):
        self.__is_str(first_name)
        self.__first_name = first_name

        self.__is_str(second_name)
        self.__second_name = second_name

        self.__is_int(age)
        self.__age = age

        self.__is_float(average_score)
        self._average_score = average_score

    def __is_str(self, any: any) -> bool or None:
        """
        Проверяет входные данные на принадлежность типу STRING
       :param text: входные данные
       :return: True or None
        """
        if not isinstance(any, str):
            raise TypeError(f'Значение {any} должно быть типа string')
        return True

    def __is_int(self, any: any) -> bool or None:
        """
        Проверяет входные данные на принадлежность типу INT
       :param any: входные данные
       :return: True or None
        """
        if not isinstance(any, int):
            raise TypeError(f'Значение {any} должно быть типа integer')
        return True

    def __is_float(self, any: any) -> bool or None:
        """
        Проверяет входные данные на принадлежность типу FLOAT или INT
       :param number: входные данные
       :return: True or None
        """
        if not isinstance(any, float):
            if not self.__is_int(any):
                raise TypeError(f'Значение {any} должно быть типа float или int')
        return True

    def get_first_name(self) -> str:
        """
       :return: значение приватного поля <имя>
        """
        return self.__first_name

    def get_second_name(self) -> str:
        """
       :return: значение приватного поля <фамилия>
        """
        return self.__second_name

    def get_age(self) -> int:
        """
       :return: значение приватного поля <возраст>
        """
        return self.__age

    def get_average_score(self) -> int:
        """
       :return: значение приватного поля <средний балл>
        """
        return self._average_score

    def set_first_name(self, new_first_name: str) -> None:
        """
        Устанавливает новое имя
       :param new_first_name: новое имя
       :return: ничего
        """
        self.__is_str(new_first_name)
        self.__first_name = new_first_name

    def set_second_name(self, new_second_name: str) -> None:
        """
        Устанавливает новою фамилию
       :param new_second_name: новая фамилия
       :return: ничего
        """
        self.__is_str(new_second_name)
        self.__first_name = new_second_name

    def set_age(self, new_age: int) -> None:
        """
        Устанавливает новое значение возраста
       :param new_age: новое значение возраста
       :return: ничего
        """
        self.__is_int(new_age)
        self.__age = new_age

    def set_average_score(self, new_average_score: int) -> None:
        """
        Устанавливает новое значение среднего балла
       :param new_average_score: новое значение среднего балла
       :return: ничего
        """
        self.__is_int(new_average_score)
        self._average_score = new_average_score


    def __str__(self):
        return f'Имя:{self.__first_name}, Фамилия:{self.__second_name}, Возраст:{self.__age}, Средний балл:{self._average_score}.'

    def __lt__(self, other):
        """ < """
        return isinstance(other,Student) and self._average_score < other._average_score

    def __le__(self, other):
        """ <= """
        return isinstance(other,Student) and self._average_score <= other._average_score

    def __eq__(self, other):
        """ == """
        return isinstance(other,Student) and self._average_score == other._average_score

    def __ne__(self, other):
        """ != """
        return isinstance(other,Student) and self._average_score != other._average_score

    def __gt__(self, other):
        """ > """
        return isinstance(other,Student) and self._average_score > other._average_score

    def __ge__(self, other):
        """ >= """
        return isinstance(other,Student) and self._average_score >= other._average_score


