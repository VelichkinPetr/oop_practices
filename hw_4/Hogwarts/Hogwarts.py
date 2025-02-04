from __future__ import annotations
import random


class Spell:


    def __init__(self,title: str, description: str, need_mp: int or float):

        if not isinstance(title,str) or not isinstance(description,str):
            raise TypeError('Название и Описание должны быть типа STR')

        if not isinstance(need_mp,int or float):
            raise TypeError('Стоимость Маны дожна быть типа INT or FLOAT')

        self.__title = title
        self.__description = description
        self.__need_mp = need_mp

    def __str__(self):
        return f'Название: {self.__title}, Эффект: {self.__description}, Стоимость Маны: {self.__need_mp}'

    def get_title(self) -> str:
        return self.__title

    def get_description(self) -> str:
        return self.__description

    def get_need_mp(self) -> int or float:
        return self.__need_mp

    def set_title(self,title: str) -> None:

        if not isinstance(title,str):
            raise TypeError('Название должно быть типа STR')

        self.__title = title

    def set_description(self, description: str) -> None:

        if not isinstance(description, str):
            raise TypeError('Описание должно быть типа STR')

        self.__description = description

    def set_need_mp(self, need_mp: str) -> None:

        if not isinstance(need_mp, int or float):
            raise TypeError('Стоимость Маны дожна быть типа INT or FLOAT')

        self.__need_mp = need_mp

    def cast(self, target: HogwartsStudent):
        return self.__title


class HogwartsStudent:


    def __init__(self, name: str, house: str, mp: int or float, spells = None):

        if not isinstance(name,str) or not isinstance(house,str):
            raise TypeError('Имя и Дом должны быть типа STR')

        if not isinstance(mp,int or float):
            raise TypeError('Количество Маны дожна быть типа INT or FLOAT')

        self.__name = name
        self.__house = house
        self.__mp = mp
        self.__spells = spells or []

    def __str__(self):
        return f'Имя: {self.__name}, Дом: {self.__house}, Мана: {self.__mp}, Заклинания: {[elem.__str__() for elem in self.__spells]}'

    def get_name(self) -> str:
        return self.__name

    def get_house(self) -> str:
        return self.__house

    def get_mp(self) -> int or float:
        return self.__mp

    def get_spells(self) -> list[Spell]:
        return self.__spells

    def set_name(self, name: str) -> None:

        if not isinstance(name, str):
            raise TypeError('Имя должно быть типа STR')

        self.__name = name

    def set_house(self, house: str) -> None:

        if not isinstance(house, str):
            raise TypeError('Дом должен быть типа STR')

        self.__house = house

    def set_mp(self, mp: str) -> None:

        if not isinstance(mp, int or float):
            raise TypeError('Количество Маны дожно быть типа INT or FLOAT')

        self.__mp = mp

    def in_spells(self, spell: Spell) -> bool:

        if not isinstance(spell, Spell):
            raise TypeError('Заклинание должно быть типа Spell')
        return spell in self.__spells

    def learn_spell(self, spell: Spell, school: Hogwarts) -> None:

        if not school.in_spells(spell):
            raise ValueError('Заклинание нет в программе обучения')

        if self.in_spells(spell):
            raise ValueError('Заклинание уже изучено')


        self.__spells.append(spell)

    def cast_spell(self, target: HogwartsStudent) -> None:

        if len(self.__spells) == 0:
            raise ValueError('Заклинаний нет')

        spell = random.choice(self.__spells)
        if self.__mp >= spell.get_need_mp():
            self.__mp -= spell.get_need_mp()
            print(f'{self.__name, self.__mp}, {spell.cast(target)}, {target.get_name(),target.get_mp()}')


class Hogwarts:


    def __init__(self, students = None, spells= None):

        self.__students = students or []
        self.__spells = spells or []

    def get_students(self) -> list[HogwartsStudent]:
        return self.__students

    def get_spells(self) -> list[Spell]:
        return self.__spells

    def in_students(self,student: HogwartsStudent) -> bool:

        if not isinstance(student, HogwartsStudent):
            raise TypeError('Студент должен быть типом HogwartsStudent')

        return student in self.__students

    def enroll_student(self, student: HogwartsStudent) -> None:

        if self.in_students(student):
            raise ValueError('Студент уже был зачислен')

        self.__students.append(student)

    def in_spells(self,spell: Spell) -> bool:

        if not isinstance(spell, Spell):
            raise TypeError('Заклинание должно быть типом Spell')

        return spell in self.__spells

    def teach_spell(self, spell: Spell) -> None:

        if self.in_spells(spell):
            raise ValueError('Заклинание есть в учебной программе')

        self.__spells.append(spell)

    def simulate_duel(self,student1: HogwartsStudent, student2: HogwartsStudent) -> None:
        """
        Симуляция дуэли происходит при соблюдении следующих условий:
        1)Участники дуэли являются Студентами школы
        2)Заклинания используемые участниками должны быть доступны для изучения в школе

        Если условия соблюдены, случайным образом выбирается, кто будет ходить первым
        Дуэль продолжается пока у обоих студентов Мана больше 0
        Победителем становится участник, у которого позже закончится Мана
        :param student1: объект класса HogwartsStudent
        :param student2: объект класса HogwartsStudent
        :return: None
        """

        if student1 == student2:
            raise Exception('Участника должно быть 2!!!')

        if not (self.in_students(student1) and (self.in_students(student2))):
            raise Exception('Участники дуэли должны быть студентами')

        first_step = random.choice([student1,student2])
        second_step = student2 if first_step == student1 else student1

        while (student1.get_mp() > 0) and (student2.get_mp() > 0):
            first_step.cast_spell(second_step)
            second_step.cast_spell(first_step)
        else:
            self.winner(student1,student2)

    def winner(self,student1: HogwartsStudent, student2: HogwartsStudent) -> None:

        if student1.get_mp() == 0 and student2.get_mp() > 0:
            print(f'Win:{student2.get_name()}')
        else:
            print(f'Win:{student1.get_name()}')