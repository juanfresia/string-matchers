import test_pattern_pattern
import tests_classic_tests
import tests_multiple_matches
import tests_no_matches
import tests_one_character
import tests_one_match
from testing_class import MATCHERS

TEST_RESULTS = "test_results"

TEST_MODULES = [tests_no_matches, tests_one_match, test_pattern_pattern, tests_multiple_matches, tests_one_character,
                tests_classic_tests]
ENABLED_TESTS = []

for _module in TEST_MODULES:
    for test in _module.ENABLED_TESTS:
        ENABLED_TESTS.append(test)


def main():
    with open("{}.md".format(TEST_RESULTS), 'w') as output:
        header = "# Results \n\n | |"
        for tag in sorted(MATCHERS.keys()):
            header += "{}|".format(tag)

        div = "|:---|" + "---:|" * (len(MATCHERS))
        output.write(header + "\n")
        output.write(div + "\n")
        for test_class in ENABLED_TESTS:
            output.write(test_class().run_all() + "\n")

        output.write("# Descriptions \n\n")
        for test_class in ENABLED_TESTS:
            _actual_class = test_class()
            output.write(
                    "## {} \n\n {}\n".format(_actual_class.get_long_test_name(), _actual_class.get_test_description()))


main()
