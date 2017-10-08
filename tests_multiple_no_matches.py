import string

from testing_multi_class import TestMultimatch


class TestMN1(TestMultimatch):
    _string = "a" * 499 + "b" * 50 + "a" * 499 + "b" * 453 + "a" * 499
    _patterns = ["a" * 500] * 10

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._patterns)
        return f(self._string, self._patterns)

    def get_expected_result(self):
        return [[] for _ in range(10)]

    def get_test_name(self):
        return "MN-1"

    def get_long_test_name(self):
        return "Multiple No-Matches 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n={} el largo del patron.
                """.format(self._iterations, len(self._string), len(self._patterns[0]))


class TestMN2(TestMultimatch):
    _string = "c" * 499 + "b" * 50 + "c" * 499 + "b" * 453 + "c" * 499
    _patterns = ["a" * 500] * 10

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._patterns)
        return f(self._string, self._patterns)

    def get_expected_result(self):
        return [[] for _ in range(10)]

    def get_test_name(self):
        return "MN-2"

    def get_long_test_name(self):
        return "Multiple No-Matches 2"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n={}.
                """.format(self._iterations, len(self._string), len(self._patterns[0]))


class TestMN3(TestMultimatch):
    _string = "a" * 4 + "b" * 555 + "a" * 4 + "b" * 1437 + "a" * 4
    _patterns = ["a" * 5] * 10

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._patterns)
        return f(self._string, self._patterns)

    def get_expected_result(self):
        return [[] for _ in range(10)]

    def get_test_name(self):
        return "MN-3"

    def get_long_test_name(self):
        return "Multiple No-Matches 3"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n={} el largo del patron (patron corto).
                """.format(self._iterations, len(self._string), len(self._patterns[0]))


class TestMN4(TestMultimatch):
    _string = "c" * 4 + "b" * 555 + "c" * 4 + "b" * 1437 + "c" * 4
    _patterns = ["a" * 5] * 10

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._patterns)
        return f(self._string, self._patterns)

    def get_expected_result(self):
        return [[] for _ in range(10)]

    def get_test_name(self):
        return "MN-4"

    def get_long_test_name(self):
        return "Multiple No-Matches 4"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n={} (Patron corto).
                """.format(self._iterations, len(self._string), len(self._patterns[0]))


class TestMN5(TestMultimatch):
    _pattern = "".join([string.ascii_lowercase[i % (len(string.ascii_lowercase))] for i in range(499)] + ["3"])
    _string = _pattern[:499] + _pattern[:499] + _pattern[:499] + _pattern[:499] + "1111"

    _patterns = [_pattern] * 10

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._patterns)
        return f(self._string, self._patterns)

    def get_expected_result(self):
        return [[] for _ in range(10)]

    def get_test_name(self):
        return "MN-5"

    def get_long_test_name(self):
        return "Multiple No-Matches 5"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

La cadena esta conformada por 4 patrones concatenados sin el ultimo caracter. El patron es periodico asi que hay varios matches parciales.
El patron es de largo n, con n={}.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestMN6(TestMultimatch):
    _string = "abcd" * 500
    _patterns = ["abca" * 25] * 10

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._patterns)
        return f(self._string, self._patterns)

    def get_expected_result(self):
        return [[] for _ in range(10)]

    def get_test_name(self):
        return "MN-6"

    def get_long_test_name(self):
        return "Multiple No-Matches 6"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

No hay 500 posibles candidatos, porque aparecen los n-1 primeros caracters del patron repetidos 500 veces cada n caracteres,
en el string, con n={} el largo del patron.
                """.format(self._iterations, len(self._string), len(self._patterns[0]))


ENABLED_TESTS = [TestMN1, TestMN2, TestMN3, TestMN4, TestMN5, TestMN6]
