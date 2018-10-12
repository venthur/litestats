from functools import lru_cache
import time


def something(a: int):
    time.sleep(a)


def something_else():
    for a in range(4):
        something(a)


@lru_cache()
def fibonacci(n: int):
    if n <= 0:
        raise ValueError('n must be positive')

    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print('Hello I am the main function')
    print(fibonacci(6))
    something_else()
    print(fibonacci(242))


if __name__ == '__main__':
    main()

