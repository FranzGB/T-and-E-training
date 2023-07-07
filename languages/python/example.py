# def power_2(n):
#     print(n)
#     return n**2


def power_3(n):
    return power_n(n, 3)


def power_6(n):
    return power_3(n) * 25


def power_n(n):
    def elevate(p):
        return n**p

    return elevate


power_2_new = power_n(2)
print(power_2_new(4))
