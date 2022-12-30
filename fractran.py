from mymath import rational, integer
from dataclasses import dataclass
from math import log


@dataclass
class fractran:
    fT: tuple[rational]
    
    def __init__(self, *fT: rational):
        self.fT = fT

    def __call__(self, n: integer) -> integer:
        if not (isinstance(n, integer) and n > integer(0)):
            raise Exception("not a positive integer")

        _n = rational(n)
        for f in self.fT:
            if (_n*f).isinteger():
                return self(integer(_n*f))

        return integer(_n)

    def input(self, *arg: integer):
        k = len(arg)
        if k < 6:
            pL = [integer(2), integer(3), integer(5), integer(7), integer(11)][:k]
        else:
            upper_bound_of_kth_prime = int(k * (log(k) + log(log(k))))
            nL = list(range(upper_bound_of_kth_prime+1))

            nL[1] = 0
            
            for n in nL:
                for m in range(2, k//n+1):
                    nL[n*m] = 0

            pL = [integer(n) for n in nL]

        _product = integer(1)
        for p, x in zip(pL, arg):
            _product *= p**x

        return self(_product)


    def sequence(self, n: integer):
        if not (isinstance(n, integer) and n > integer(0)):
            raise Exception("not a positive integer")

        _n = rational(n)
        while True:
            for f in self.fT:
                if (_n*f).isinteger():
                    yield integer(_n*f)
                    _n *= f
                    break
            else:
                break

        yield integer(_n)


