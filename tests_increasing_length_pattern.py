import random

from testing_class import Test


class TestIP1(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * 250
        self._pattern = self._string

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IP-1"

    def get_long_test_name(self):
        return "Increasing Length Test 1"

    def get_test_description(self):
        return """
Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIP2(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * (9000 // 2) + "bb" * 250
        self._pattern = self._string

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IP-2"

    def get_long_test_name(self):
        return "Increasing Length Test 2"

    def get_test_description(self):
        return """
Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIP3(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * (99000 // 2) + "bb" * 250
        self._pattern = self._string

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IP-3"

    def get_long_test_name(self):
        return "Increasing Length Test 3"

    def get_test_description(self):
        return """
Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIP4(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "bb" * (999000 // 2) + "bb" * 250
        self._pattern = self._string

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IP-4"

    def get_long_test_name(self):
        return "Increasing Length Test 4"

    def get_test_description(self):
        return """
Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


ALPHABET = "bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$123456789|#&()?"


class TestIP5(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(500)])
        self._pattern = self._string

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IP-5"

    def get_long_test_name(self):
        return "Increasing Length Test 5"

    def get_test_description(self):
        return """
Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIP6(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(9500)])
        self._pattern = self._string

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IP-6"

    def get_long_test_name(self):
        return "Increasing Length Test 6"

    def get_test_description(self):
        return """
Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIP7(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(99500)])
        self._pattern = self._string

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IP-7"

    def get_long_test_name(self):
        return "Increasing Length Test 7"

    def get_test_description(self):
        return """
Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


class TestIP8(Test):
    def __init__(self):
        super().__init__()
        self._iterations = 1
        self._pattern = "b" * 499 + "a"
        self._string = self._pattern + "".join([random.choice(ALPHABET) for _ in range(999500)])
        self._pattern = self._string

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return [0]

    def get_test_name(self):
        return "IP-8"

    def get_long_test_name(self):
        return "Increasing Length Test 8"

    def get_test_description(self):
        return """
Match en el principio de la cadena de largo {}
        """.format(len(self._string), len(self._pattern))


ENABLED_TESTS = [TestIP1, TestIP2, TestIP3, TestIP4, TestIP5, TestIP6, TestIP7, TestIP8]
