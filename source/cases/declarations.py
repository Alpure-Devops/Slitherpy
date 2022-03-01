from .base import Case as BaseCase
from ..assertion import Assert, Assertion
from ..utils import callMethodFromString

from dataclasses import dataclass

class Case(BaseCase):
    class _Results(BaseCase._Results):
        @dataclass
        class CaseError:
            pass

    def _runDeclaration(self, name: str, *args, **kwargs):
        return callMethodFromString(self.Declarations, name, *args, **kwargs)

    def __init__(self, assertion: Assertion=Assert) -> None:
        #* Setup Case Result and Assertion Class
        self.Result = self._initResult()
        self._assertion_class = assertion

        #* Fetch Tests
        test_list = self._fetchTests(self.Tests, {
            'ignore-attributes': True,
            'ignore-classes': True,
            'ignore-dunder': True,
            'ignore-type': True
        })

        self._runDeclaration('setup')

        #* Execute Iterate Through Tests
        for testname in test_list:
            self._runDeclaration('beforeTestRuns')

            #* Execute Test
            self._executeTest(testname)

            self._runDeclaration('afterTestRuns')

        self._runDeclaration('teardown')
        
