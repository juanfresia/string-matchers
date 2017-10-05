from testing_class import Test


class TestPP1(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern
    _iterations = 4000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "PP-1"

    def get_long_test_name(self):
        return "Pattern to Pattern 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un match. La cadena es el patron mismo.

No hay mas de un solo posible candidato, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}..
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestPP2(Test):
    _pattern = "a" * 499 + "b" * 1
    _string = _pattern
    _iterations = 4000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "PP-2"

    def get_long_test_name(self):
        return "Pattern to Pattern 2"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un match. La cadena es el patron mismo.

Hay varios posibles candidatos, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={} repetido n-1 veces.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestPP3(Test):
    _pattern = "a" * 499 + "b" * 1 + "a" * 250 + "b" * 250
    _string = _pattern
    _iterations = 2000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "PP-3"

    def get_long_test_name(self):
        return "Pattern to Pattern 3"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un match. La cadena es el patron mismo.

Hay varios posibles candidatos, solo hay 2 caracteres en la cadena, y se presentan de forma intercalada
en el patron de largo n={}.
                """.format(self._iterations, len(self._string), len(self._pattern))


ENABLED_TESTS = [TestPP1, TestPP2, TestPP3]
