class TxtFormatter:
    def __init__(self, data):
        self._data = data
        self._idx = 0

    def next(self):
        if self._idx >= len(self._data):
            return None
        line = f"{self._data[self._idx]['name']}: {self._data[self._idx]['grade']}"
        self._idx += 1
        return line