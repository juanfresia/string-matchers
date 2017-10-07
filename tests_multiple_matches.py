from testing_class import Test


class TestMM1(Test):
    _pattern = "a" + "b" * 498 + "c"
    _string = _pattern * 4
    _iterations = 1000

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


ENABLED_TESTS = [TestMM1]
