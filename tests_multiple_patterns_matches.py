from testing_multi_class import TestMultimatch


class TestMP1(TestMultimatch):
    _pattern1 = "a" + "b" * 498 + "c"
    _pattern2 = "a" + "b" * 498 + "a"

    _string = (_pattern1 + _pattern2) * 2

    _patterns = [_pattern1, _pattern2] * 5

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._patterns)
        return f(self._string, self._patterns)

    def get_expected_result(self):
        result = []
        for j in range(len(self._patterns)):
            result1 = []
            for i in range(j % 2, 4, 2):
                result1.append(len(self._patterns[j]) * i)
            result.append(result1)

        return result

    def get_test_name(self):
        return "MP-1"

    def get_long_test_name(self):
        return "Multiple Pattern Matches Test 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay 4 matches un match.

No hay mas de solo 4 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}, siendo la cadena una concatenacion de 4 veces el patron.
                """.format(self._iterations, len(self._string), len(self._patterns[0]))


ENABLED_TESTS = [TestMP1]
