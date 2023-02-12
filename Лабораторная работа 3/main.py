class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __setattr__(self, key, value):
        if self.__dict__.get(key) is None or self.__dict__.get(key) is None:
            object.__setattr__(self, key, value)
        else:
            if key != "name" and key != "author":
                object.__setattr__(self, key, value)
            else:
                raise AttributeError("Этот атрибут неизменяем")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        if pages < 0:
            raise ValueError("Число страниц должно быть больше 0")
        else:
            self.pages = pages
        if type(pages) is not int:
            raise TypeError("Число страниц должно относиться к типу int")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        if duration < 0:
            raise ValueError("Продолжительность должна быть больше 0")
        else:
            self.duration = duration
        if type(duration) is not float:
            raise TypeError("Продолжительность должна относиться к типу float")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
