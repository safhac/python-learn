"""class BaseWorker:
    def __int__(self):
        self.counter = 0

    def work(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

# answer:
# in BaseWorker
#       the base work method is decorated with @abstractmethod to ensure implementation
#       BaseWorker.work inspects caller to ensure invocation location
#       it calls a private method _do_work to mask access to count
#       use inspect

    """
# fix the base worker so implementations can be trusted.
import sys
import inspect
import warnings
from abc import abstractmethod, ABC


class BaseWorker(ABC):
    def __init__(self):
        self._counter = 0

    def __getattribute__(self, item):
        if item == "work":
            self._BaseWorker__do_work()
        return super().__getattribute__(item)

    @property
    def counter(self):
        return self._counter

    def __do_work(self):
        caller = inspect.stack()[1][3]
        if "__getattribute__" not in caller:
            warnings.warn("built in descriptor, no need to explicitly call worker()")
        else:
            self._counter += 1

    @abstractmethod
    def work(self):
        return self.__do_work()

    def get_counter(self):
        return self._counter


class MyWorker(BaseWorker):

    def work(self):
        # super().work() # will not work
        print("hello")


#
mw = MyWorker()
try:
    mw.counter += 2
except:
    print("can't do that")
mw.work()
mw.work()
print(mw.get_counter())
