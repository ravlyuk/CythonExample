import sys
import time
from loguru import logger

from cython_scripts import fibonacci_cython
from python_scripts import fibonacci_python

logger.remove(0)
logger.add(sys.stderr, format="<blue>{time:YYYY-MM-DD HH:mm:ss}</blue> <green>{message}</green>", colorize=True)


def test_speed(func, name: str, num: int, repeat: int) -> float:
    start = time.time()
    result: int = func(num, repeat)
    finish = time.time()
    spent_time = round(finish - start, 2)
    logger.debug(f'Час виконання {name}: {spent_time}, результат: {result}')
    return spent_time


def main(times: int = 5):
    deltas = []
    for i in range(1, times + 1):
        logger.debug(f'== Тест №{i} ==')
        params = {'num': 50, 'repeat': 100 ** 3}
        speed_python = test_speed(name='Python', func=fibonacci_python.test, **params)
        speed_cython = test_speed(name='Cython', func=fibonacci_cython.test, **params)
        delta = int(speed_python / speed_cython)
        deltas.append(delta)
        logger.debug(f'Cython швидший в {delta} раз')
    avg = int(sum(deltas) / len(deltas))
    logger.debug(f'Тестування завершено! В середньому Cython швидший в {avg} раз')


if __name__ == '__main__':
    main()