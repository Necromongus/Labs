# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2


def print_result(func_to_decorate):
    def decorated_func(*args, **kwargs):
        result = func_to_decorate(*args, **kwargs)
        print(func_to_decorate.__name__)
        if isinstance(result, list):
            for x in result:
                if isinstance(x, tuple):
                    if len(x) == 2:
                        print("{}, зарплата {}".format(x[0], x[1]))
                else:
                    print(x)
            # print(*(x for x in result))
        elif isinstance(result, dict):
            for key in result.keys():
                print(key, "=", result[key])
            # print(*(("\n{} = {}".format(key, result[key])) for key in result.keys()))
        else:
            print(result)
        return result
    return decorated_func
