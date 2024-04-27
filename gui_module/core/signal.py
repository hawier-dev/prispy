class Signal:
    def __init__(self):
        self._slots = []

    def connect(self, slot):
        if slot not in self._slots:
            self._slots.append(slot)

    def disconnect(self, slot):
        try:
            self._slots.remove(slot)
        except ValueError:
            pass

    def emit(self, *args, **kwargs):
        for slot in self._slots:
            slot(*args, **kwargs)
