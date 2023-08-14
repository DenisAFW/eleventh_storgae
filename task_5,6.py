# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:

    def __init__(self, height: int, width=None):
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def get_perimetr(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return self.width * self.height

    def __add__(self, other):

        perimetr = self.get_perimetr() + other.get_perimetr()
        side_a = perimetr // 6
        side_b = (perimetr - side_a * 2) // 2

        return Rectangle(side_a, side_b)

    def __sub__(self, other):

        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        side_a = perimetr // 6
        side_b = (perimetr - side_a * 2) // 2

        return Rectangle(side_a, side_b)

    """Дандер методы сравнения площадей"""

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() <= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() >= other.get_area()


spam = Rectangle(1, 9)
eggs = Rectangle(7)

add_reg = spam + eggs
sub_reg = spam - eggs
eq_reg = spam == eggs
ne_reg = spam != eggs
gt_reg = spam > eggs
ge_reg = spam <= eggs
lt_reg = spam < eggs
le_reg = spam >= eggs

print(f'{sub_reg.width = }, {sub_reg.height =}')
print(f'{add_reg.width = }, {add_reg.height =}')
print(f'Площади равны? -> {eq_reg},\nПлощади не равны? -> {ne_reg},\n'
      f'Площадь первого прямоугольника больше? -> {gt_reg},\nПлощадь меньше либо равна второй площади? -> {ge_reg},\n'
      f'Площадь меньше второй площади? -> {lt_reg},\nПлощадь больше или равна второй площади? -> {le_reg}')

# ● __eq__ - равно, =
# ● __ne__ - не равно, !=
# ● __gt__ - больше, >
# ● __ge__ - не больше, меньше или равно, <=
# ● __lt__ - меньше, <
# ● __le__ - не меньше, больше или равно, >=
