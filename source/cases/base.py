from ..assertion import Assert, Assertion
from ..status import Status
from ..utils import mapClass

from dataclasses import dataclass, field
from types import FunctionType


class Case:
    class _Results:
        @dataclass
        class TestResult:
            test_name: str = field(default_factory=str)
            status_type: str = field(default_factory=str)
            status: object = field(default_factory=object)
            test_breakdown: list[str] = field(default_factory=list)

        @dataclass()
        class CaseResult:
            case_name: str = field(default_factory=str)
            tests: list[object] = field(default_factory=list)

    class Test:
        def __init__(self, name, assertion_object: Assertion):
            if assertion_object is None:
                self.Assert = None
            else:
                self.Assert = assertion_object()
            self.name = name
    
    def _executeTest(self, name:str) -> _Results.TestResult:
        def test_decorator(func) -> FunctionType:
            def wrapper() -> Status:
                test_obj = self.Test(name, self._assertion_class)

                try:
                    returned_from_test = func(test_obj)
                except AssertionError as assert_exception:
                    returned_from_test = Status("test-fail", assert_exception )
                except Exception as exception:
                    returned_from_test = Status("unexpected-error", exception)

                #* Format Test Results
                test_result = Case._Results.TestResult(test_name=name)

                if isinstance(returned_from_test, Status):
                    test_result.status_type = returned_from_test.getType()
                    test_result.status = returned_from_test
                else:
                    test_result.status_type = "test-pass"
                    test_result.status = Status("test-pass", {})

                    if test_obj.Assert is None:
                        test_result.test_breakdown = []
                    else:
                        test_result.test_breakdown = test_obj.Assert.assert_status
                        
                        for assert_status in test_obj.Assert.assert_status:
                            if assert_status == "fail":
                                test_result.status_type = "test-fail"
                                test_result.status = Status("test-fail", {})
                                break

                return test_result
            return wrapper
            
        test_result = test_decorator(getattr(self.Tests, name))()
        self.Result.tests.append(test_result)
        return test_result

    def _fetchTests(self, cls, options):
        return mapClass(cls, options)

    def _initResult(self) -> _Results.CaseResult:
        return self._Results.CaseResult(
            case_name=self.__class__.__name__
        )

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

        #* Execute Iterate Through Tests
        for testname in test_list:
            #* Execute Test
            self._executeTest(testname)


   
    

    