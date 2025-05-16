import functools
from typing import Any, Callable


def strict(func: Callable) -> Callable:
    """
    Декоратор, проверяющий соответствие типов аргументов аннотациям функции.

    :param func: Декорируемая функция.
    :return: Обёрнутая функция с проверкой типов.
    """
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        for (value, (name, expected_type)) in zip(args, func.__annotations__.items()):
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"Аргумент '{name}' должен быть {expected_type.__name__}, получен {type(value).__name__}"
                )
        return func(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    """
    Складывает два целых числа.

    :param a: Первое слагаемое.
    :param b: Второе слагаемое.
    :return: Сумма a и b.
    """
    return a + b


#print(sum_two(1, 2))  # >>> 3
#print(sum_two(1, 2.4))  # >>> TypeError
