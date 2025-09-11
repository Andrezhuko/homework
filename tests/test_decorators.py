from src.decorators import func_one, func_two, log


def test_function_by_decorator_one(capsys):
    func_one(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "func_one ok \n\n"
    func_one(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "func_one error ZeroDivisionError . Inputs: (1, 0), {}\n\n"


def test_function_by_decorator_two():
    file_name = "logs/log.txt"
    log(filename=file_name)

    result = func_two(1, 2)
    assert result == 0.5
    with open(file_name, "r", encoding="utf-8") as file:
        last_list = file.readlines()
        assert last_list[-1] == "func_two ok \n"
    result = func_two(1, 0)

    with open(file_name, "r", encoding="utf-8") as file:
        last_list = file.readlines()
        assert last_list[-1] == "func_two error ZeroDivisionError . Inputs: (1, 0), {}\n"
