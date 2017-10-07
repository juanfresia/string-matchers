from testing_class import Test


class TestOC1(Test):
    _pattern = "a" * 500
    _string = "a" * 2000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-1"

    def get_long_test_name(self):
        return "One Character Test 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOC2(Test):
    _pattern = "a"
    _string = "a" * 2000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-2"

    def get_long_test_name(self):
        return "One Character Test 2"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron (patron corto).
                """.format(self._iterations, len(self._string), len(self._pattern))


ENABLED_TESTS = [TestOC1, TestOC2]
