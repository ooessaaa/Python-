import math
def nested_sqrt_list():
    nested_list = [[math.sqrt(x) for x in range(100, 999)] for _ in range(5)]
    return nested_list