from .base import Case as BaseCase
from ..assertion import Assertion
from ..utils import callMethodFromString

class Case(BaseCase):
    def _runDeclaration_(self, name: str, *args, **kwargs):
        return callMethodFromString(self.Declarations, name, *args, **kwargs)

    def _initCase_(self, assertion: Assertion):
        #* Setup Case Result and Assertion Class
        self.Result = self._initResult_()
        self._assertion_class = assertion

        #* Fetch Tests
        test_list = self._fetchTests_(self.Tests, {
            'ignore-attributes': True,
            'ignore-classes': True,
            'ignore-dunder': True,
            'ignore-type': True
        })

        self._runDeclaration_('setup')
        for testname in test_list:
            self._runDeclaration_('beforeTestRuns')
            self._executeTest_ (testname)
            self._runDeclaration_('afterTestRuns')
        self._runDeclaration_('teardown')
