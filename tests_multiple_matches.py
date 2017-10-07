from testing_class import Test


class TestMM1(Test):
    _pattern = "a" + "b" * 498 + "c"
    _string = _pattern * 4

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        result = []
        for i in range(4):
            result.append(len(self._pattern) * i)
        return result

    def get_test_name(self):
        return "MM-1"

    def get_long_test_name(self):
        return "Multiple Matches Test 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay 4 matches un match.

No hay mas de solo 4 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}, siendo la cadena una concatenacion de 4 veces el patron.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestMM2(Test):
    _pattern = "a" + "b" * 498 + "a"
    _string = _pattern * 4

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        result = []
        for i in range(4):
            result.append(len(self._pattern) * i)
        return result

    def get_test_name(self):
        return "MM-2"

    def get_long_test_name(self):
        return "Multiple Matches Test 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio y al final del
patron de largo n={}, siendo la cadena una concatenacion de 4 veces el patron.
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestMM3(Test):
    _pattern = "a" + "b" * 248 + "c"
    _string = (_pattern + _pattern[:len(_pattern) - 1] + "d") * 4

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        result = []
        for i in range(0, 8, 2):
            result.append(len(self._pattern) * i)
        return result

    def get_test_name(self):
        return "MM-3"

    def get_long_test_name(self):
        return "Multiple Matches Test 3"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}, siendo la cadena una concatenacion de 4 veces el patron mas 4 veces un match parcial.
                    """.format(self._iterations, len(self._string), len(self._pattern))


class TestMM4(Test):
    _pattern = "a" + "b" * 248 + "c"
    _string = (_pattern[:len(_pattern) - 1] + "d" + _pattern) * 4

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        result = []
        for i in range(1, 9, 2):
            result.append(len(self._pattern) * i)
        return result

    def get_test_name(self):
        return "MM-4"

    def get_long_test_name(self):
        return "Multiple Matches Test 4"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}, siendo la cadena una concatenacion de 4 veces un match parcial mas 4 veces el patron.
                    """.format(self._iterations, len(self._string), len(self._pattern))


ENABLED_TESTS = [TestMM1, TestMM2, TestMM3, TestMM4]
