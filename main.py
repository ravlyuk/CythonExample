import sys
import time
from loguru import logger

from cython_scripts import fibonacci_cython
from python_scripts import fibonacci_python

logger.remove(0)
logger.add(sys.stderr, format="<blue>{time:YYYY-MM-DD HH:mm:ss}</blue> <green>{message}</green>", colorize=True)


def round_time(long_number: float) -> float:
    return round(long_number, 2)


def test_speed(func, name: str, num: int, repeat: int) -> float:
    start = time.time()
    result: int = func(num, repeat)
    finish = time.time()
    spent_time = finish - start
    logger.debug(f'Час виконання {name}: {round_time(spent_time)}, результат: {result}')
    return spent_time


def main(times: int = 5):
    deltas = []
    for i in range(times):
        logger.debug(f'== Тест №{i + 1} ==')
        params = {'num': 50, 'repeat': 100 ** 3}
        speed_python = test_speed(name='Python', func=fibonacci_python.test, **params)
        speed_cython = test_speed(name='Cython', func=fibonacci_cython.test, **params)
        delta = int(speed_python / speed_cython)
        logger.debug(f'Cython швидший в {round_time(delta)} раз')
        deltas.append(delta)
    avg_speed = int(sum(deltas) / len(deltas))
    logger.debug(f'Тестування завершено! В середньому Cython швидший в {avg_speed} раз!')


if __name__ == '__main__':
    main()
