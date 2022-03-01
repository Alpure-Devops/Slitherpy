from source.assertion import Assert
from source.cases.base import Case

class BaseTests(Case):
    class Tests:
        def assertTest1(test:Case.Test):
            assert True

        def assertTest2(test:Case.Test):
            assert False

class AssertTests(Case):
    class Tests:
        def standalone(test: Case.Test):
            test.Assert.Pass()

        def standalone2(test: Case.Test):
            test.Assert.Fail()

        def blankTest(test: Case.Test):
            pass

        def errorTest(test: Case.Test):
            with test.Assert.PassOnError(Exception):
                raise Exception("test")
            
        def errorTest2(test: Case.Test):
            raise Exception("Warning!!!")


results = BaseTests(assertion = None).Result
print(f"Base Tests: {results}")

results = AssertTests(assertion = Assert).Result
print(f"Assert Tests: {results}")