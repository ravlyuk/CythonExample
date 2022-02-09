def test(numb: int, repeat: int) -> int:
    f1 = f2 = 1
    for _ in range(repeat):
        f1 = f2 = 1
        for _ in range(numb - 2):
            f1, f2 = f2, f1 + f2
    return f2
