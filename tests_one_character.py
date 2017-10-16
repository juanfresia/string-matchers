from testing_class import Test


class TestOC1(Test):
    _pattern = "a" * 500
    _string = "a" * 2000

    def __init__(self):
        super().__init__()

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

    def __init__(self):
        super().__init__()

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


class TestOC3(Test):
    _pattern = "aa"
    _string = "a" * 2000

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-3"

    def get_long_test_name(self):
        return "One Character Test 3"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron (patron corto de largo par).
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOC4(Test):
    _pattern = "aaa"
    _string = "a" * 2000

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-4"

    def get_long_test_name(self):
        return "One Character Test 4"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron (patron corto de largo impar).
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOC5(Test):
    _pattern = "aaa"
    _string = "a" * 2000

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-5"

    def get_long_test_name(self):
        return "One Character Test 5"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron (patron corto limite ventana DC3).
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOC6(Test):
    _pattern = "aaaa"
    _string = "a" * 2000

    def __init__(self):
        super().__init__()

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-6"

    def get_long_test_name(self):
        return "One Character Test 6"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron (patron limite+1 ventana DC3).
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOC7(Test):
    _pattern = "a" * 500
    _string = "a" * 10000

    def __init__(self):
        super().__init__()

    def run(self, f):
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-7"

    def get_long_test_name(self):
        return "One Character Test 7"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron (patron corto).
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOC8(Test):
    _pattern = "a" * 500
    _string = "a" * 100000

    def __init__(self):
        super().__init__()

    def run(self, f):
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-8"

    def get_long_test_name(self):
        return "One Character Test 8"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron (patron corto de largo par).
                """.format(self._iterations, len(self._string), len(self._pattern))


class TestOC9(Test):
    _pattern = "a" * 500
    _string = "a" * 1000000

    def __init__(self):
        super().__init__()

    def run(self, f):
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [x for x in range(len(self._string) - len(self._pattern) + 1)]

    def get_test_name(self):
        return "OC-9"

    def get_long_test_name(self):
        return "One Character Test 9"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n={} el largo del patron (patron corto de largo impar).
                """.format(self._iterations, len(self._string), len(self._pattern))


ENABLED_TESTS = [TestOC1, TestOC2, TestOC3, TestOC4, TestOC5, TestOC6, TestOC7, TestOC8, TestOC9]
