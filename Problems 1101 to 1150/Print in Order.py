import threading


class Foo:
    def __init__(self):
        self.__condition = threading.Condition()
        self.__first_executed = False
        self.__second_executed = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        with self.__condition:
            # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.__first_executed = True
            self.__condition.notifyAll()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        with self.__condition:
            while not self.__first_executed:
                self.__condition.wait()
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.__second_executed = True
            self.__condition.notifyAll()


    def third(self, printThird: 'Callable[[], None]') -> None:

        with self.__condition:
            while not self.__second_executed:
                self.__condition.wait()
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
            self.__condition.notifyAll()
