from contextlib import contextmanager
import threading
import thread

class TimeoutException(Exception):
    def __init__(self, msg=''):
        self.msg = msg

@contextmanager
def time_limit(seconds, msg=''):
    timer = threading.Timer(seconds, lambda: thread.interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt:
        raise TimeoutException("Timed out for operation {}".format(msg))
    finally:
        # if the action ends in specified time, timer is canceled
        timer.cancel()

def execute_no_matter_how(method, time):
    try:
        with time_limit(time, 'sleep'):
            method()
    except TimeoutException:
        return False
    else:
        return True