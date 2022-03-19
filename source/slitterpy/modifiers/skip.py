from ..status import Status

def Skip(condition:bool=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return Status("test-skipped", {})
            else:
                func(*args, **kwargs)
            return None
        return wrapper
    return decorator