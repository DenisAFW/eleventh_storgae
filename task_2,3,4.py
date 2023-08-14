# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """"Документация класса Архив"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arch = []

        cls._instance.list_arch.append([args])

        return cls._instance

    def __init__(self, text: str, number: int):
        self.text = text
        self.number = number

    def __str__(self):
        return f"Текущий текст строки: {self.text}, число строки: {self.number}"

    def __repr__(self):
        return f'Archive({self.text}, {self.number})'


spam = Archive("Ночной страж", 45)
print(spam)
print(f'{spam.text}, {spam.number}')
spam = Archive("Ночной дозор", 485)
print(f'{spam.text}, {spam.number}')

print(f'{spam.list_arch = }')
"""Только в таком случае выводится дандер метод репр, когд он указывается в принт методе"""
print(repr(spam))
print(f'{spam = }')

# help(Archive)
