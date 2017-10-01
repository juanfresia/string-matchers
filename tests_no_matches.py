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
    _pattern = "a" * 500
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


ENABLED_TESTS = [TestNM1, TestNM2, TestNM3, TestNM4]
