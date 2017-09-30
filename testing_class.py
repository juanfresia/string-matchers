import time

from karpRabin import karpRabin
from naive import string_matching_naive
from zbox import string_matching_zcajas

MATCHERS = {'Naive': string_matching_naive,
            'Karp Rabin': karpRabin,
            'Z Box': string_matching_zcajas,
            'Nothing _Test Only_': lambda x, y: None}


class Test:
    def run(self, f):
        raise NotImplementedError

    def get_expected_result(self):
        raise NotImplementedError

    def get_test_name(self):
        raise NotImplementedError

    def get_long_test_name(self):
        raise NotImplementedError

    def get_test_description(self):
        raise NotImplementedError

    def cron_test(self, f):
        initial_time = time.time()
        result = self.run(f)
        end_time = time.time()

        run_time = end_time - initial_time

        return result, run_time

    def run_all(self):
        result_string = "|[{}](#{})|".format(self.get_test_name(), self.get_long_test_name().replace(" ", "-"))

        for tag in sorted(MATCHERS.keys()):
            result, run_time = self.cron_test(MATCHERS[tag])
            status = "OK" if result == self.get_expected_result() else "ERROR"

            result_string += "{: 7.6} - ({})|".format(run_time, status)

        return result_string