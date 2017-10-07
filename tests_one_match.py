from testing_class import Test


class TestOM1(Test):
    _pattern = "a" + "b" * 499
    _string = "b" * 500 + _pattern + "b" * 1000

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [500]

    def get_test_name(self):
        return "OM-1"

    def get_long_test_name(self):
        return "One Match Test 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un match.

No hay mas de un solo posible candidato, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOM2(Test):
    _pattern = "a" * 499 + "b"
    _string = "b" * 500 + _pattern + "b" * 1000

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [500]

    def get_test_name(self):
        return "OM-2"

    def get_long_test_name(self):
        return "One Match Test 2"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={} de forma repetida..
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOM3(Test):
    _pattern = "a" + "b" * 499
    _string = "c" * 500 + _pattern + "c" * 1000

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [500]

    def get_test_name(self):
        return "OM-3"

    def get_long_test_name(self):
        return "One Match Test 3"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un match.

No hay mas de un solo posible candidato, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOM4(Test):
    _pattern = "a" * 499 + "b"
    _string = "c" * 500 + _pattern + "c" * 1000

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [500]

    def get_test_name(self):
        return "OM-4"

    def get_long_test_name(self):
        return "One Match Test 4"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={} de forma repetida..
                """.format(self._iterations, len(self._string), len(self._pattern))


ENABLED_TESTS = [TestOM1, TestOM2, TestOM3, TestOM4]
