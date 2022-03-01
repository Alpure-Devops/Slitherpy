from source.cases.declarations import Case

class CoreTests(Case):
    class Declarations:
        def setup():
            print("setup:")

        def teardown():
            print("teardown:")

        def beforeTestRuns():
            print("beforeTestRuns:")

        def afterTestRuns():
            print("afterTestRuns:")

    class Tests:
        def standalone(test: Case.Test):
            test.Assert.Pass()
            print("hi")

        def standalone2(test: Case.Test):
            test.Assert.Fail()

        def errorTest(test: Case.Test):
            with test.Assert.PassOnError(Exception):
                raise Exception("test")

results = CoreTests().Result
print(f"Test Results: {results}")