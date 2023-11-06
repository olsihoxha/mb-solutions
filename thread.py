import threading


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=()):
        super(ThreadWithReturnValue, self).__init__(target=target, args=args)
        self._return_value = None

    def run(self):
        if self._target is not None:
            self._return_value = self._target(*self._args)

    def join(self, timeout=None):
        super(ThreadWithReturnValue, self).join()
        return self._return_value
