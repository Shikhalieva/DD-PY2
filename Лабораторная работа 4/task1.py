import doctest


class PNTransition:
    """
    Класс описывает p-n переход, его свойства,а также содержит набор методов, который позволяет
    посчитать прямой и обратный ток через переход
    """
    def __init__(self, p_prop: list, n_prop: list, voltage: float):
        """
        :param p_prop: Свойства материала с p-проводимостью
        :param n_prop: Свойства материала с n-проводимостью
        :param voltage: Напряжение через транзистор в Вольтах

        Пример:
        >>> ex1 = PNTransition(["Si", 1.5*10**10], ["C", 1.2*10**10], -14.4) # создаем экземпляр класса - контакт SiC
        """
        self.p_prop = p_prop
        self.n_prop = n_prop
        self.voltage = voltage

    def __str__(self):
        return f"p-n переход. Свойства п/п p-типа: {self.p_prop}, свойства п/п n-типа: {self.n_prop}"

    def __repr__(self):
        return f"{self.__class__.__name__}(p_prop={self.p_prop!r}, n_prop={self.n_prop!r}, voltage={self.voltage!r})"

    def to_define_direct(self):
        """
        Метод определяет прямой ток через контакт п|п и п/п
        :return: Возвращает значение обратного тока

        Пример:
        >>> ex2 = PNTransition(["Si", 1.5*10**10], ["C", 1.2*10**10], -14.4) # создаем экземпляр класса - контакт SiC
        >>> ex2.to_define_direct() # рассчитываем прямой ток через p-n переход
        """
        ...

    def to_define_back(self):
        """
        Метод определяет обратный ток через контакт п|п и п/п
        :return: Возвращает значение обратного тока

        Пример:
        >>> ex3 = PNTransition(["In", 1.5*10**18], ["P", 10**16], 2.4) # создаем экземпляр класса - контакт InP
        >>> ex3.to_define_back() # рассчитываем обратный ток через p-n переход
        """
        ...


class SchottkyContact:
    """
    Класс описывает контакт Шотки, его свойства,а также содержит набор методов, которые позволяют
    посчитать прямой ток через переход
    """
    def __init__(self, p_prop: list, n_prop: list, voltage: float):
        """
        :param p_prop: Свойства материала с p-проводимостью
        :param n_prop: Свойства материала с n-проводимостью
        :param voltage: Напряжение через транзистор в Вольтах
        """
        super().__init__(p_prop=p_prop, n_prop=n_prop, voltage=voltage)

    @staticmethod
    def to_define_back():
        """
        Метод перегружаем, так как через контакт Шотки обратного тока нет
        """
        return f"Обратный ток через диод не идет"


if __name__ == "__main__":
    doctest.testmod()
