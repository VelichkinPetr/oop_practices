from __future__ import annotations
from abc import ABC,abstractmethod


class Farm:


    def __init__(self, name:str,
                 location: str,
                 fields: list[Field] = None,
                 storages: list[Storage] = None,
                 green_houses: list[GreenHouse] = None,
                 seeds: list[ASeed] = None,
                 equipments: list[AFarmEquipment] = None,
                 animals: list[AFarmAnimal] = None):
        self.__name = name
        self.__location = location
        self.__fields = fields or []
        self.__storages = storages or []
        self.__green_houses = green_houses or []
        self.__seeds = seeds or []
        self.__equipments = equipments or []
        self.__animals = animals or []

    def work(self):
        return 'Ферма работает!'


class Field:


    def __init__(self, name: str,
                 width:float,
                 depth: float,
                 location: str,
                 inventory: list[any] = None):
        self.__name = name
        self.__width = width
        self.__depth = depth
        self.__location = location
        self.__inventory = inventory or []


    def sow(self, any):
        return self.__inventory.append(any)

    def harvested_crop(self, any):
        if any not in self.__inventory:
            raise ValueError('На поле такого нет!')
        return self.__inventory.remove(any)


class Storage:


    def __init__(self, number: int,
                 width:float,
                 height: float,
                 depth: float,
                 location: str,
                 inventory: list[any] = None):
        self.__number = number
        self.__height = height
        self.__width = width
        self.__depth = depth
        self.__location = location
        self.__inventory = inventory or []


    def add(self, any):
        return self.__inventory.append(any)

    def pop(self, any):
        if any not in self.__inventory:
            raise ValueError('На складе такого нет!')
        return self.__inventory.pop( self.__inventory.index(any) )


class GreenHouse:


    def __init__(self, number: str,
                 width:float,
                 height:float,
                 depth: float,
                 location: str,
                 inventory: list[any] = None):
        self.__number = number
        self.__width = width
        self.__height = height
        self.__depth = depth
        self.__location = location
        self.__inventory = inventory or []


    def sow(self, any):
        return self.__inventory.append(any)

    def harvested_crop(self, any):
        if any not in self.__inventory:
            raise ValueError('В Теплице такого нет!')
        return self.__inventory.remove(any)


class ASeed(ABC):


    def __init__(self, name: str,
                 count:float,
                 maturation_time: float,
                 seasonality: str,
                 status: bool = False):
        self._name = name
        self._count = count
        self._maturation_time = maturation_time
        self._status = status
        self._seasonality = seasonality

    @abstractmethod
    def sow(self):pass

    @abstractmethod
    def is_ready(self):pass


class GrainCorp(ASeed):


    def __init__(self, name: str,
                 count:float,
                 maturation_time: float,
                 seasonality: str,
                 status: bool,
                 type: str):
        self.__type = type
        super().__init__(name,count,maturation_time,seasonality,status)


    def is_ready(self):
        self._status = True
        return self._status

    def sow(self):
        if self._status:
            return 'Зерно собрано!'


class Vegetable(ASeed):

    def __init__(self, name: str,
                 count: float,
                 maturation_time: float,
                 seasonality: str,
                 status: bool,
                 type: str):
        super().__init__(name, count, maturation_time, seasonality, status)
        self.__type = type

    def is_ready(self):
        self._status = True
        return self._status

    def sow(self):
        if self.is_ready():
            return 'Овощи собраны!'


class AFarmEquipment(ABC):


    def __init__(self, engine: str,
                 power_reserver:float):
        self._engine = engine
        self._power_reserver = power_reserver


    @abstractmethod
    def work(self):pass


class Harvester(AFarmEquipment):


    def __init__(self, engine: str,
                 power_reserver:float,
                 traction_moment: float):
        super().__init__(engine,power_reserver)
        self.__traction_moment = traction_moment

    def work(self):
        return 'Комбайн работает!'


class Tractor(AFarmEquipment):


    def __init__(self, engine: str,
                 power_reserver:float,
                 traction_moment: float):
        super().__init__(engine,power_reserver)
        self.__traction_moment = traction_moment

    def work(self):
        return 'Трактор работает!'


class AFarmAnimal(ABC):


    def __init__(self, nick_name: str,
                 age: float):
        self._nick_name = nick_name
        self._age = age

    @abstractmethod
    def feed(self):pass

class Cow(AFarmAnimal):

    def __init__(self, nick_name: str,
                 age: float,
                 milk_volume: float):
        super().__init__(nick_name,age)
        self.__milk_volume = milk_volume

    def feed(self):
        return 'Корова ест!'


class Chicken(AFarmAnimal):

    def __init__(self, nick_name: str,
                 age: float,
                 count_egg: int):
        super().__init__(nick_name, age)
        self.__count_egg = count_egg

    def feed(self):
        return 'Курица ест!'


class Pig(AFarmAnimal):

    def __init__(self, nick_name: str,
                 age: float,
                 weight: int):
        super().__init__(nick_name, age)
        self.__weight = weight

    def feed(self):
        return 'Свинья ест!'


class Sheep(AFarmAnimal):

    def __init__(self, nick_name: str,
                 age: float,
                 wool_volume: int):
        super().__init__(nick_name, age)
        self.__wool_volume = wool_volume

    def feed(self):
        return 'Овца ест!'