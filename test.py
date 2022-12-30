from fractran import fractran
from mymath import rational, integer
from math import log2, log




print(integer(4) + integer(2))





if False:
    primegame = fractran(
        rational(17, 91),
        rational(78, 85),
        rational(19, 51),
        rational(23, 38),
        rational(29, 33),
        rational(77, 29),
        rational(95, 23),
        rational(77, 19),
        rational(1, 17),
        rational(11, 13),
        rational(13, 11),
        rational(15, 2),
        rational(1, 7),
        rational(55, 1)
    )

    for y in primegame.sequence(integer(2)):
        print(y)
        if log2(int(y)).is_integer():
            input()

if False:
    addition = fractran(
        rational(3, 2)
    )

    a = integer(int(input()))
    b = integer(int(input()))
    print(addition.input(a, b).log(integer(3)))

if False:
    subtraction = fractran(
        rational(1, 6)
    )

    a = integer(int(input()))
    b = integer(int(input()))
    if a < b:
        print(subtraction.input(a, b).log(integer(3)))
    else:
        print(subtraction.input(a, b).log(integer(2)))

if False:
    subtraction = fractran(
        rational(5, 6),
        rational(5, 2),
        rational(5, 3)
    )

    a = integer(int(input()))
    b = integer(int(input()))
    print(subtraction.input(a, b).log(integer(5)))

if True:
    multiplication = fractran(
        rational(455, 33),
        rational(11, 13),
        rational(1, 11),
        rational(3, 7),
        rational(11, 2),
        rational(1, 3)
    )

    a = integer(int(input()))
    b = integer(int(input()))
    print(multiplication.input(a, b).log(integer(5)))

if False:
    division = fractran(
        rational(91, 66),
        rational(11, 13),
        rational(1, 33),
        rational(85, 11),
        rational(57, 119),
        rational(17, 19),
        rational(11, 17),
        rational(1, 3)
    )

    a = integer(int(input()))
    b = integer(int(input()))
    print(division.input(a, b, integer(0), integer(0), integer(1))) #5**quotient * 7**remainder
