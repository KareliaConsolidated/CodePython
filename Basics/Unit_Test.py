def nearest_square(num):
    """Return the nearest perfect square that is less than or equal to num"""
    root = 0
    while (root + 1) ** 2 <= num:
        root += 1
    return root ** 2