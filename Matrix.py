# GITHUB: https://github.com/Guilherme-De-Marchi/Neural-Network-v2
# License: MIT

from functools import reduce

class Matrix:
    def __init__(self, target, size: tuple=(0, 0)):
        '''param: target -> list or int or float
        param: size[optional] -> tuple(number of rows, number of columns) just if target is instance of int or float'''

        assert isinstance(target, (list, int, float)), 'param :target: is not valid'

        if isinstance(target, list):
            assert len(target) and all([isinstance(row, list) for row in target]), 'param :target: is not a valid matrix'
            assert all([all([isinstance(item, (int, float)) for item in row]) for row in target]), 'items of param :target: are not int or float'
            assert sum([len(row) for row in target]) / len(target) == len(target[0]), 'param :target: is not a uniform matrix'

        else:
            assert len(size) == 2 and all([isinstance(num, (int, float)) for num in size]) and all(size), 'param: size is not valid'

            target = [[target for column in range(size[1])] for row in range(size[0])]

        self._content = target

    def transposed(self):
        '''return: Matrix object'''
        result = []
        for column in range(self._size[1]):
            result.append([])
            for row in self._content:
                result[column].append(row[column])

        return self.__class__(result)

    @classmethod
    def iterateTwoMatrices(cls, function, a: 'Matrix', b: 'Matrix'=[], additional=0):
        '''param: function(params -> a, b[optional], additional[optional])'''

        result = []
        for row_a in a._content:
            result.append([])
            for row_b in b._content:
                calc = function(row_a, row_b, additional)
                result[-1].append(calc)

        return cls(result)

    @classmethod
    def zipIterateTwoMatrices(cls, function, a: 'Matrix', b: 'Matrix'=[], additional=0):
        '''param: function(params -> a, b[optional], additional[optional])'''

        result = []
        for row_a, row_b in zip(a._content, b._content):
            result.append([])
            for value_a, value_b in zip(row_a, row_b):
                calc = function(value_a, value_b, additional)
                result[-1].append(calc)

        return cls(result)

    def __add__(self, other):
        return self.__class__.add(self, other)

    @classmethod
    def add(cls, a: 'Matrix', b: 'Matrix'):
        '''return: Matrix object'''

        assert isinstance(a, cls) and isinstance(b, cls), 'invalid addition'
        assert a._size == b._size, 'invalid addition between matrices with different sizes'

        return cls.zipIterateTwoMatrices(lambda value_a, value_b, *_: value_a + value_b, a, b)

    def __sub__(self, other):
        return self.__class__.sub(self, other)

    @classmethod
    def sub(cls, a: 'Matrix', b: 'Matrix'):
        '''return: Matrix object'''

        assert isinstance(a, cls) and isinstance(b, cls), 'invalid subtraction'
        assert a._size == b._size, 'invalid subtraction between matrices with different sizes'

        return cls.zipIterateTwoMatrices(lambda value_a, value_b, *_: value_a - value_b, a, b)

    def __mul__(self, other):
        return self.__class__.mul(self, other)

    @classmethod
    def mul(cls, a, b):
        '''param: a -> Matrix
        param: b -> Matrix or int or float
        return: Matrix object'''

        assert isinstance(a, cls) and isinstance(b, (cls, int, float)), 'invalid multiplication'

        if isinstance(b, (int, float)):
            b = cls(b, sorted(a._size, reverse=True))

        assert a._size[0] == b._size[1], 'invalid multiplication between matrices'

        return cls.iterateTwoMatrices(
            lambda row_a, row_b, *_: sum([value_a * value_b for value_a, value_b in zip(row_a, row_b)]),
            a,
            b.transposed()
        )

    @classmethod
    def hadamardProduct(cls, a, b):
        '''param: a -> Matrix
        param: b -> Matrix or int or float
        return: Matrix object'''

        assert isinstance(a, cls) and isinstance(b, (cls, int, float)), 'invalid multiplication'

        if isinstance(b, (int, float)):
            b = cls(b, sorted(a._size, reverse=True))

        assert a._size[0] == b._size[1], 'invalid multiplication between matrices'

        return cls.zipIterateTwoMatrices(lambda *args: reduce(lambda x, y: x * y, args[:-1]), a, b)

    def __str__(self):
        return str(self._content)

    @property
    def _size(self) -> tuple:
        '''return: tuple(rows, columns)'''

        return (len(self._content), len(self._content[0]))