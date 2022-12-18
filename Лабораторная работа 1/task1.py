import doctest


class BubbleGumLoveIs:
    """
    Класс описывает жевательные резинки Love is
    """

    def __init__(self, taste: str, color: str, number_message: int):
        """
        :param taste: Вкус
        :param color: Цвет
        :param number_message: Номер послания

        Пример:
        >>> bubble_1 = BubbleGumLoveIs("apple and lemon", "yellow", 99)
        """
        self.number_message = None
        if not isinstance(taste, str):
            raise TypeError("Данные должны принадлежать к типу str")
        self.taste = taste
        if not isinstance(color, str):
            raise TypeError("Данные должны принадлежать к типу str")
        self.color = color
        self.change_number(number_message)

    def change_number(self, new_number: int):
        """
        Метод позволяет заменить послание

        :param new_number: Номер новго послания
        :raise ValueErroe: Если номер послания отрицателен, выводим ошибку
        :raise TypeErroe: Если тип данных new_number не принадлкежит к int, выводим ошибку

        Пример:
        >>> bubble_2 = BubbleGumLoveIs("banana and strawberry", "blue", 14)
        >>> bubble_2.change_number(5)
        """
        self.number_message = None
        if not isinstance(new_number, int):
            raise TypeError("Данные должны принадлежать к типу int")
        if new_number < 0:
            raise ValueError("Номер послания не может быть отрицательным")
        self.number_message = new_number
        ...

    def get_properties(self):
        """
        Метод выводит все свойства объекта
        """
        print(self.color, self.taste, self.number_message)
        ...


class Dot:
    """
    Класс описывает координаты материальной точки
    """
    def __init__(self, x: float, y: float):
        """
        :param x: Координата по оси абсцисс
        :param y: Координата по оси ординат

        Пример:
        >>> dot1 = Dot(5.0, 10.0) # инициализируем экземпляр класса
        """
        self.x = None
        self.y = None
        self.change_x(x)
        self.change_y(y)

    def change_x(self, new_x: float):
        """
        Метод позволяет менять параметр x
        :param new_x: Новое значение по оси абсцисс
        :raise TypeErroe: Если тип данных new_x не принадлкежит к float, выводим ошибку

        Пример:
        >>> dot2 = Dot(2.0, 3.0) # инициализируем экземпляр класса (точка с координатами (2;3))
        >>> dot2.change_x(5.0) # меняем координату x
        """
        if not isinstance(new_x, float):
            raise TypeError("Данные должны принадлежать к типу float")
        self.x = new_x
        ...

    def change_y(self, new_y: float):
        """
        Метод позволяет менять параметр y
        :param new_y: Новое значение по оси ординат
        :raise TypeErroe: Если тип данных new_x не принадлкежит к float, выводим ошибку

        Пример:
        >>> dot3 = Dot(4.0, 6.0) # инициализируем экземпляр класса (точка с координатами (4;6))
        >>> dot3.change_y(-9.0) # меняем координату y
        """
        if not isinstance(new_y, float):
            raise TypeError("Данные должны принадлежать к типу float")
        self.y = new_y
        ...


class Lamp:
    """
    Класс описывает свойства и работу лампочки
    """
    def __init__(self, brightness: float, color: str):
        """
        :param brightness: Яркость лампочки
        :param color: Цвет лампочки

        Пример:
        >>> lamp1 = Lamp(0.33, "white")
        """
        self.brightness = None
        self.color = None
        self.change_brightness(brightness)
        self.change_color(color)

    def change_brightness(self, new_brightness: float):
        """
        Метод позволяет менять яркость лампочки
        :param new_brightness: Новое значение яркости
        :raise TypeErroe: Если тип данных new_brightness не принадлежит к float, выводим ошибку

        Пример:
        >>> lamp2 = Lamp(0.45, "red") # инициализируем экземпляр класса (лампочка с яркостью 0.45 и красного цвета)
        >>> lamp2.change_brightness(0.65) # меняем яркость
        """
        if not (0 < new_brightness < 1):
            raise ValueError("Яркость не может быть больше 1 и меньше 0")
        if not isinstance(new_brightness, float):
            raise TypeError("Данные должны принадлежать к типу float")
        self.brightness = new_brightness
        ...

    def change_color(self, new_color: str):
        """
        Метод позволяет менять цвет лампочки
        :param new_color: Новый цвет лампочки
        :raise TypeErroe: Если тип данных new_color не принадлежит к str, выводим ошибку

        Пример:
        >>> lamp3 = Lamp(0.55, "blue") # инициализируем экземпляр класса (лампочка с яркостью 0.55 и голубого цвета)
        >>> lamp3.change_color("orange") # меняем цвет лампочки
        """
        if not isinstance(new_color, str):
            raise TypeError("Данные должны принадлежать к типу str")
        self.color = new_color
        ...


if __name__ == "__main__":
    doctest.testmod()
