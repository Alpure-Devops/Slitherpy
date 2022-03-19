class Assertion:
    def __init__(self) -> None:
        self.assert_status:list[str] = []

class Assert(Assertion):
    def Pass(self):
        self.assert_status.append("pass")

    def Fail(self):
        self.assert_status.append("fail")

    def PassIf(self, condition):
        if condition:
            self.assert_status.append("pass")
        else:
            self.assert_status.append("fail")

    def FailIf(self, condition):
        if not condition:
            self.assert_status.append("fail")
        else:
            self.assert_status.append("pass")

    class _PassOnError:
        def __init__(self, error, assertCls):
            self.assert_error = error
            self.assertCls = assertCls

        def __enter__(self):
            pass

        def __exit__(self, errortype, _, __):
            if self.assert_error is errortype:
                self.assertCls.assert_status.append("pass")
            else:
                self.assertCls.assert_status.append("fail")
            return True
    
    class _FailOnError:
        def __init__(self, error, assertCls):
            self.assert_error = error
            self.assertCls = assertCls

        def __enter__(self):
            pass

        def __exit__(self, errortype, _, __):
            if self.assert_error is errortype:
                self.assertCls.assert_status.append("fail")
            else:
                self.assertCls.assert_status.append("pass")
            return True

    def PassOnError(self, error) -> _PassOnError:
        return self._PassOnError(error, self)

    def FailOnError(self, error) -> _FailOnError: 
        return self._FailOnError(error, self)