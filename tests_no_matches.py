import string

from testing_class import Test


class TestNM1(Test):
    _string = "a" * 499 + "b" * 50 + "a" * 499 + "b" * 453 + "a" * 499
    _pattern = "a" * 500
    _iterations = 1000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "NM-1"

    def get_long_test_name(self):
        return "No Matches Test 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n={} el largo del patron.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestNM2(Test):
    _string = "c" * 499 + "b" * 50 + "c" * 499 + "b" * 453 + "c" * 499
    _pattern = "a" * 500
    _iterations = 1000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "NM-2"

    def get_long_test_name(self):
        return "No Matches Test 2"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n={}.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestNM3(Test):
    _string = "a" * 4 + "b" * 555 + "a" * 4 + "b" * 1437 + "a" * 4
    _pattern = "a" * 5
    _iterations = 1000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "NM-3"

    def get_long_test_name(self):
        return "No Matches Test 3"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n={} el largo del patron (patron corto).
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestNM4(Test):
    _string = "c" * 4 + "b" * 555 + "c" * 4 + "b" * 1437 + "c" * 4
    _pattern = "a" * 5
    _iterations = 1000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "NM-4"

    def get_long_test_name(self):
        return "No Matches Test 4"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n={} (Patron corto).
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestNM5(Test):
    _pattern = "".join([string.ascii_lowercase[i % (len(string.ascii_lowercase))] for i in range(499)] + ["3"])
    _string = _pattern[:499] + _pattern[:499] + _pattern[:499] + _pattern[:499] + "1111"
    _iterations = 1000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "NM-5"

    def get_long_test_name(self):
        return "No Matches Test 5"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

La cadena esta conformada por 4 patrones concatenados sin el ultimo caracter. El patron es periodico asi que hay varios matches parciales.
El patron es de largo n, con n={}.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestNM6(Test):
    _string = "abcd" * 500
    _pattern = "abca" * 25
    _iterations = 1000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "NM-6"

    def get_long_test_name(self):
        return "No Matches Test 6"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

No hay 500 posibles candidatos, porque aparecen los n-1 primeros caracters del patron repetidos 500 veces cada n caracteres,
en el string, con n={} el largo del patron.
                """.format(self._iterations, len(self._string), len(self._pattern))


ENABLED_TESTS = [TestNM1, TestNM2, TestNM3, TestNM4, TestNM5, TestNM6]
