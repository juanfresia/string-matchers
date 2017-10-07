from testing_class import Test


class TestCT1(Test):
    _pattern = "ana"
    _string = "banana"

    def __init__(self):
        super().__init__()
        self._iterations = self._iterations * 1000 // len(self._string)

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [1, 3]

    def get_test_name(self):
        return "CT-1"

    def get_long_test_name(self):
        return "Classic Test 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre "banana" buscando el patron "ana". Ejemplo de DC3
                """.format(self._iterations)


class TestCT2(Test):
    _pattern = "yaba"
    _string = "banana"

    def __init__(self):
        super().__init__()
        self._iterations = self._iterations * 1000 // len(self._string)

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "CT-2"

    def get_long_test_name(self):
        return "Classic Test 2"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre "banana" buscando el patron "yaba". Ejemplo de DC3
                """.format(self._iterations)


class TestCT3(Test):
    _pattern = "yabba"
    _string = "yabbadabbado"

    def __init__(self):
        super().__init__()
        self._iterations = self._iterations * 1000 // len(self._string)

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "CT-3"

    def get_long_test_name(self):
        return "Classic Test 3"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre "yabbadabbado" buscando el patron "yabba". Ejemplo de DC3
                """.format(self._iterations)


class TestCT4(Test):
    _pattern = "bba"
    _string = "yabbadabbado"

    def __init__(self):
        super().__init__()
        self._iterations = self._iterations * 1000 // len(self._string)

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [2, 7]

    def get_test_name(self):
        return "CT-4"

    def get_long_test_name(self):
        return "Classic Test 4"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre "yabbadabbado" buscando el patron "bba". Ejemplo de DC3
                """.format(self._iterations)


class TestCT5(Test):
    _pattern = "dabba"
    _string = "yabbadabbado"

    def __init__(self):
        super().__init__()
        self._iterations = self._iterations * 1000 // len(self._string)

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [5]

    def get_test_name(self):
        return "CT-5"

    def get_long_test_name(self):
        return "Classic Test 5"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre "yabbadabbado" buscando el patron "dabba". Ejemplo de DC3
                """.format(self._iterations)


class TestCT6(Test):
    _pattern = "ana"
    _string = "yabbadabbado"

    def __init__(self):
        super().__init__()
        self._iterations = self._iterations * 1000 // len(self._string)

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "CT-6"

    def get_long_test_name(self):
        return "Classic Test 6"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre "yabbadabbado" buscando el patron "ana". Ejemplo de DC3
                """.format(self._iterations)


ENABLED_TESTS = [TestCT1, TestCT2, TestCT3, TestCT4, TestCT5, TestCT6]
