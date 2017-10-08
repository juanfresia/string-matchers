import random

from testing_class import Test


class TestIL1(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * 250

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * (9000 // 2) + "bb" * 250

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * (99000 // 2) + "bb" * 250

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * (999000 // 2) + "bb" * 250

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * (9999000 // 2) + "bb" * 250

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(500)])

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(9500)])

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(99500)])

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(999500)])

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
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(9999500)])

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


ENABLED_TESTS = [TestIL1, TestIL2, TestIL3, TestIL4, TestIL6, TestIL7, TestIL8, TestIL9]
