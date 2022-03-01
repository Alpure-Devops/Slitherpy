class Status:
    def __init__(self, status_type: str, data:object = None) -> None:
        self._status_type = status_type
        self.data = data

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Status):
            return self._status_type == __o._status_type
        return False

    def getType(self):
        return self._status_type