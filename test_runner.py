from testing_class import MATCHERS, Test


class TestNM1(Test):
    _string = "a" * 499 + "b" * 50 + "a" * 499 + "b" + "a" * 499
    _pattern = "a" * 500
    _iterations = 1000

    def run(self, f):
        for _ in range(self._iterations - 1):
            f(self._string, self._pattern)
        return f(self._string, self._pattern)

    def get_expected_result(self):
        return []

    def get_test_name(self):
        return "NM-1"

    def get_long_test_name(self):
        return "No Matches Test 1"

    def get_test_description(self):
        return """
Corre {} veces el string matcher sobre una cadena de largo {} en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n={} el largo del patron.
                """.format(self._iterations, len(self._string), len(self._pattern))


ENABLED_TESTS = [TestNM1]


def main():
    with open("output.md", 'w') as output:
        header = "| |"
        for tag in sorted(MATCHERS.keys()):
            header += "{}|".format(tag)

        div = "|" + ":---|" * (len(MATCHERS) + 1)
        output.write(header + "\n")
        output.write(div + "\n")
        for test_class in ENABLED_TESTS:
            output.write(test_class().run_all() + "\n")

        for test_class in ENABLED_TESTS:
            _actual_class = test_class()
            output.write(
                    "## {} \n\n {}\n".format(_actual_class.get_long_test_name(), _actual_class.get_test_description()))


main()
