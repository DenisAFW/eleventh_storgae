# # Создайте класс Матрица. Добавьте методы для:
# # ○ вывода на печать,
# # ○ сравнения,
# # ○ сложения,
# # ○ *умножения матриц
from random import randint


class Matrix:
    _rows: int = None
    _cols: int = None
    _matrix: list[list[int, float]] = None

    def __init__(self, matrix: list[list[int, float]]):
        self._rows = len(matrix)
        self._cols = len(matrix[0])
        self._matrix = matrix

    def __add__(self, other):
        """Складывание матриц"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        new_matrix = [[(self._matrix[i][j] + other._matrix[i][j])
                       for j in range(self._cols)] for i in range(self._rows)]
        return Matrix(new_matrix)

    def __mul__(self, other):
        """Умножение матриц"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        new_matrix = [[(self._matrix[j][i] * other._matrix[i][j])
                       for j in range(self._cols)] for i in range(self._rows)]
        return Matrix(new_matrix)

    def __eq__(self, other):
        """Сравнение """
        if self is other:
            return True
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for j in range(self._rows):
            for i in range(self._cols):
                if self._matrix[j][i] != other._matrix[j][i]:
                    return False
        return True

    def __ne__(self, other):
        """Возвращает True если одна матрица неравна другой"""
        return not self.__eq__(other)

    def __str__(self):
        """Печать для чтения пользователем"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self._matrix]) + '\n'

    def __repr__(self):
        """Печать для чтения программистом"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self._matrix]) + '\n'


def main():
    """Генератор матрицы"""
    matrix_1 = [[randint(1, 10) for j in range(5)] for i in range(5)]
    matrix_2 = [[randint(1, 10) for j in range(5)] for i in range(5)]
    mat_1 = Matrix(matrix_1)
    mat_2 = Matrix(matrix_2)

    print(mat_1)
    print(mat_2)
    print(repr(mat_1))
    print(f'Сложение матриц \n{mat_1 + mat_2}')
    print(f'Умножение матриц \n{mat_1 * mat_2}')


if __name__ == '__main__':
    main()
