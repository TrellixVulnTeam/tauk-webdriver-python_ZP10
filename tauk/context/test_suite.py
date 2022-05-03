import typing

from tauk.context.test_case import TestCase
from tauk.exceptions import TaukException
from tauk.utils import get_filtered_object


class TestSuite:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.name = None
        self.class_name = None
        self._test_cases: typing.List[TestCase] = []

    def __getstate__(self):
        state = get_filtered_object(self, include_private=True)
        return state

    def __deepcopy__(self, memodict={}):
        return self

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def class_name(self) -> str:
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        self._class_name = class_name

    @property
    def test_cases(self):
        return self._test_cases

    def add_testcase(self, testcase: TestCase):
        for test in self.test_cases:
            if test.method_name == testcase.method_name:
                raise TaukException('cannot use TaukListener and Observer() for the same test')

        self.test_cases.append(testcase)

    def get_test_case(self, test_name) -> TestCase:
        for test in self.test_cases:
            if test.custom_name == test_name or test.method_name == test_name:
                return test
        return None
