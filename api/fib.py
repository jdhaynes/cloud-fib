def compute(index: int):
    if index < 2:
        return 1
    else:
        return compute(index - 2) + compute(index - 1)
