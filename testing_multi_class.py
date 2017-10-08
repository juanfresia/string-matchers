from dc3 import multiple_string_matching_dc3
from string_encoder import encode_string
from testing_class import Test


def do_nothing(text, patterns):
    text = encode_string(text)
    for pattern in patterns:
        pattern = encode_string(pattern)
    return None


MATCHERS = {'Baseline': do_nothing,
            'DC3': multiple_string_matching_dc3}

VERBOSE = False


class TestMultimatch(Test):
    _iterations = 10

    def run_all(self):
        result_string = "|[{}](#{})|".format(self.get_test_name(), self.get_long_test_name().replace(" ", "-").lower())

        for tag in sorted(MATCHERS.keys()):
            results, run_time = self.cron_test(MATCHERS[tag])
            if results:
                for result in results:
                    result.sort()

            status = "OK" if results == self.get_expected_result() else "ERROR"

            if status != "OK" and VERBOSE:
                print("Error: <{2}> expected:{1}, got:{0}".format(results, self.get_expected_result(), tag))

            result_string += "{:03.6f} - ({})|".format(run_time, status)

        return result_string
