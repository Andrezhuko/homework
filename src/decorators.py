from typing import Any, Callable


def write_log(filename: str | None, message: str) -> None:
    """функция, которая принимает путь и сообщение и выводит текст в терминал или записывает в файл"""
    if filename:
        with open(filename, "a") as file:
            file.write(message)
    else:
        print(message)


def log(filename: str | None = None) -> Callable:
    """декоратор для логирования и выполнения функций"""

    def decorator_log(func: Callable) -> Any:
        """внутренний декоратор применяемой фукнции"""

        # @wraps(func)
        def wrapper(*arg: tuple, **kwargs: dict) -> Any:
            """обертка выполняющая логирование"""
            func_name = func.__name__
            try:
                func_result = func(*arg, **kwargs)
                message = f"{func_name} ok \n"
                write_log(filename, message)
                return func_result
            except Exception as error:
                name_error = type(error).__name__
                message = f"{func_name} error {name_error} . Inputs: {arg}, {kwargs}\n"
                write_log(filename, message)

        return wrapper

    return decorator_log


@log()
def func_one(a, b):
    return a / b


@log(filename="logs/log.txt")
def func_two(a, b):
    return a / b
