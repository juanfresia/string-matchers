from naive import string_matching_naive
from testing_multi_class import TestMultimatch


class TestTEC1(TestMultimatch):
    _patterns = ["gata"]

    def __init__(self):
        super().__init__()
        with open("ecoli.dat") as input_file:
            self._string = input_file.read()

    def run(self, f):
        return f(self._string, self._patterns)

    _result = None

    def _get_result(self):
        result = []
        for pattern in self._patterns:
            result.append(string_matching_naive(self._string, pattern))
        return result

    def get_expected_result(self):
        if not self._result:
            self._result = self._get_result()
        return self._result

    def get_test_name(self):
        return "TEC-1"

    def get_long_test_name(self):
        return "Tests over EColi 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay 4 matches un match.

No hay mas de solo 4 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}, siendo la cadena una concatenacion de 4 veces el patron.
                """.format(self._iterations, len(self._string), len(self._patterns))


class TestTEC2(TestMultimatch):
    _patterns = ["gata", "cata", "agcttcagtgcacgtacgtatgc", "acgtcagtcgacgtagtc", "aaagcgacgactttgt"] * 10

    def __init__(self):
        super().__init__()
        with open("ecoli.dat") as input_file:
            self._string = input_file.read()

    def run(self, f):
        return f(self._string, self._patterns)

    _result = None

    def _get_result(self):
        result = []
        for pattern in self._patterns:
            result.append(string_matching_naive(self._string, pattern))
        return result

    def get_expected_result(self):
        if not self._result:
            self._result = self._get_result()
        return self._result

    def get_test_name(self):
        return "TTG-2"

    def get_long_test_name(self):
        return "Tests over EColi 2"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay 4 matches un match.

No hay mas de solo 4 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n={}, siendo la cadena una concatenacion de 4 veces el patron.
                """.format(self._iterations, len(self._string), len(self._patterns))


ENABLED_TESTS = [TestTEC1, TestTEC2]
