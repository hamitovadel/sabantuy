def fibonacci(num):
    try:
        num = int(num)
        f1 = f2 = 1
        if num == 0:
            return {'result': 0}
        for _ in range(2, num):
            f1, f2 = f2, f1 + f2
        return {'result': f2}
    except ValueError:
        return {'result': 'error'}

