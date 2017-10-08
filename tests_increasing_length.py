import random

from testing_class import Test


class TestIL1(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "ab" * 250

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-1"

    def get_long_test_name(self):
        return "Increasing Length Test 1"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIL2(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "aa" * (99000 // 2) + "ab" * 250

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-2"

    def get_long_test_name(self):
        return "Increasing Length Test 2"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIL3(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "ab" * (9999000 // 2) + "ab" * 250

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-3"

    def get_long_test_name(self):
        return "Increasing Length Test 3"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIL4(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "ab" * (999999000 // 2) + "ab" * 250

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-4"

    def get_long_test_name(self):
        return "Increasing Length Test 4"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIL5(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "ab" * (99999999000 // 2) + "ab" * 250

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-5"

    def get_long_test_name(self):
        return "Increasing Length Test 5"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


ALPHABET = "bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$123456789|#&()?"


class TestIL6(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "".join([random.choice(ALPHABET) for _ in range(500)])

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-6"

    def get_long_test_name(self):
        return "Increasing Length Test 6"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIL7(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "".join([random.choice(ALPHABET) for _ in range(99500)])

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-7"

    def get_long_test_name(self):
        return "Increasing Length Test 7"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIL8(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "".join([random.choice(ALPHABET) for _ in range(9999500)])

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-8"

    def get_long_test_name(self):
        return "Increasing Length Test 8"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIL9(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "".join([random.choice(ALPHABET) for _ in range(999999500)])

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-9"

    def get_long_test_name(self):
        return "Increasing Length Test 9"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestILA(Test):
    _pattern = "a" + "b" * 499
    _string = _pattern + "".join([random.choice(ALPHABET) for _ in range(99999999500)])

    def __init__(self):
        super().__init__()
        self._iterations = 1

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IL-A"

    def get_long_test_name(self):
        return "Increasing Length Test A"

    def get_test_description(self):
        return """
        Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))
