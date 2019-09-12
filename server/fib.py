def fib_sequence(num: int):
    """
    Transform given number according to Fibonacci sequence, according to formula Fn = Fn-1 + Fn-2
    :param num: number for sequence in int type.
    :return: transformed number
    """
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        return fib_sequence(num - 1) + fib_sequence(num - 2)
