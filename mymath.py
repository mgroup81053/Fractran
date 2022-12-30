from typing import Generator





# set based on ZFC
class mset: ...
class mset:
    def __init__(self, *arg):
        self.elementL: list[mset] = []

        if len(arg)==1 and isinstance(arg[0], Generator):
            elements = arg[0]
        else:
            elements = arg

        for element in elements:
            self.add(element)

    def add(A, element):
        if not isinstance(element, mset):
            raise Exception("invalid element")

        if element not in A:
            A.elementL.append(element)

    def is_subset_of(A, other): # A⊆B ⇔ ∀a∈A a∈B
        for self_element in A:
            if self_element not in other:
                return False

        return True

    def S(A): # successor: S(A) = {A ∪ {A}}
        return A | mset(A)

    def antiS(A):
        if A == mset():
            raise Exception("no antisuccessor")

        _ordered_elementL = sorted(A.elementL, key=lambda a: a.rank())
        aL, antisuccessor = _ordered_elementL[:-1], _ordered_elementL[-1]

        for a in aL:
            if a not in antisuccessor:
                raise Exception("no antisuccessor")

        return antisuccessor

    def Union(A): # axiom of the union: ∀A∃U∀X∀x (x∈X ∧ X∈A ⇒ x∈U)
        _temp = mset()

        for X in A:
            for x in X:
                _temp.add(x)

        return _temp

    def P(A): # axiom of the power set: ∀A∃P∀a (a⊆A ⇒ a∈P) #NOTE: is there any better method?
        _temp = mset()

        m = len(A.size())
        inclusion_table = [i for i in range(2**m)]
        for case in inclusion_table:
            _temp.add(mset(a for i, a in enumerate(A) if case & (1 << i)))

        return _temp

    @staticmethod
    def ordinal(m: int):
        if not (isinstance(m, int) and m >= 0):
            raise Exception("invalid m for ordinal")

        _temp = mset()
        for _ in range(m):
            _temp = _temp.S()

        return _temp

    def size(A):
        return mset.ordinal(len(A.elementL)) #NOTE: is there any better idea?

    def rank(A) -> mset:
        if A == mset():
            return mset()
        else:
            max_element_rank = max([a.rank() for a in A])
            return max_element_rank.S()

    def isordinal(A):
        if A == mset():
            return True

        _ordered_elementL = sorted(A.elementL, key=lambda a: a.size()) #NOTE: is there a better idea?

        if _ordered_elementL[0] != mset():
            return False

        for m, mth_natural in enumerate(_ordered_elementL):
            for larger_natural in _ordered_elementL[m+1:]:
                if mth_natural not in larger_natural:
                    return False

        return True

    def isnatural(A):
        return A.isordinal()

    def isinteger(A):
        return A.isnatural()

    def __str__(self):
        return "{" + ", ".join(str(element) for element in self) + "}"

    def __int__(A):
        if A.isinteger():
            return int(len(A.elementL))
        else:
            raise Exception("not an integer")

    def __iter__(self):
        return iter(self.elementL)

    def __eq__(A, B): # A=B ⇔ A⊆B ∧ B⊆A
        if isinstance(B, mset):
            return A.is_subset_of(B) and B.is_subset_of(A)
        else:
            raise Exception("invalid comparison")

    def __gt__(A, B): # for orinal A,B: A>B ⇔ B⊂A ⇔ B∈A
        if isinstance(B, mset) and B.isordinal():
            return B in A
        else:
            raise Exception("invalid comparison")

    def __ge__(A, B): # for orinal A,B: A>=B ⇔ B⊆A ⇔ B∈A ∨ B=A
        if isinstance(B, mset) and B.isordinal():
            return B.is_subset_of(A)
        else:
            raise Exception("invalid comparison")

    def __lt__(A, B): # for orinal A,B: A<B ⇔ A⊂B ⇔ A∈B
        if isinstance(B, mset) and B.isordinal():
            return A in B
        else:
            raise Exception("invalid comparison")

    def __le__(A, B): # for orinal A,B: A>=B ⇔ A⊆B ⇔ A∈B ∨ A=B
        if isinstance(B, mset) and B.isordinal():
            return A.is_subset_of(B)
        else:
            raise Exception("invalid comparison")

    def __ne__(A, B): # A≠B ⇔ A⊈B ∨ B⊈A
        if isinstance(B, mset):
            return not A.is_subset_of(B) or not B.is_subset_of(A)
        else:
            raise Exception("invalid comparison")

    def __and__(A, B): # A∩B = {a∈A | a∈B} (from axiom schema of specification)
        if isinstance(B, mset):
            return mset(a for a in A if a in B)
        else:
            raise Exception("invalid intersection")

    def __or__(A, B): # A∪B = ⋃{A, B} (from axiom of the union)
        if isinstance(B, mset):
            return mset.Union([A, B])
        else:
            raise Exception("invalid intersection")

    def __sub__(A, B): # A∩B = {a∈A | a∉B} (from axiom schema of specification)
        if isinstance(B, mset):
            return mset(a for a in A if a not in B)
        else:
            raise Exception("invalid difference")




# natural numbers based on set (von neumann structure)
# very slow and inefficient
class natural: ...
class natural:
    def __init__(self, val):
        if not(\
            isinstance(val, int) and val >= 0\
            or getattr(val, "isnatural", lambda: False)()):

            raise Exception("invalid value for natural")

        _temp = mset()
        for _ in range(int(val)): #FIXME: is there any better idea?
            _temp = _temp.S()

        self.val = _temp

    def isnatural(m) -> bool:
        return True

    def isinteger(m) -> bool:
        return True

    def isrational(m) -> bool:
        return True

    def isreal(m) -> bool:
        return True

    @staticmethod
    def gcd(m: natural, n: natural): # euclidean algorithm
        m, n = max(m,n), min(m,n)
        while m != natural(0) and n != natural(0):
            m -= n * (m//n)
            m, n = n, m

        return m

    @staticmethod
    def reduce(m: natural, n: natural):
        gcd_value = natural.gcd(m, n)
        m //= gcd_value
        n //= gcd_value

        return m, n

    def S(m):
        return natural(m.val.S())

    def antiS(m):
        return natural(m.val.antiS())

    def __str__(m):
        return str(int(m.val))

    def __pos__(m):
        return natural(m)

    def __abs__(m):
        return natural(m)

    def __add__(m, n) -> natural:
        if isinstance(n, natural):
            if n == natural(0):
                return natural(m)
            else:
                return (m + n.antiS()).S()
        else:
            raise Exception("invalid addition")

    def __sub__(m, n):
        if isinstance(n, natural) and m >= n:
            return natural(int(m) - int(n)) #FIXME
        else:
            raise Exception("invalid subtraction")

    def __mul__(m, n) -> natural:
        if isinstance(n, natural):
            if n == natural(0):
                return natural(0)
            else:
                return (m * n.antiS()) + m
        else:
            raise Exception("invalid multiplication")

    def __truediv__(m, n):
        if isinstance(n, natural) and int(m) % int(n) == 0: #FIXME
            return natural(int(m) // int(n)) #FIXME
        else:
            raise Exception("invalid division")

    def __floordiv__(m, n):
        if isinstance(n, natural):
            return natural(int(m) // int(n)) #FIXME
        else:
            raise Exception("invalid division")

    def __mod__(m, n):
        if isinstance(n, natural):
            return natural(int(m) % int(n)) #FIXME
        else:
            raise Exception("invalid modular")

    def __pow__(m, n):
        if isinstance(n, natural):
            return natural(int(m)**int(n)) #FIXME
        else:
            raise Exception("invalid power operation")

    def __gt__(m, n): # m > n ⇔ ∃k∈N k≠0 ∧ n+k=m
        if isinstance(n, natural):
            return int(m) > int(n) #FIXME
        else:
            raise Exception("invalid size comparison")
        
    def __ge__(m, n):
        if isinstance(n, natural):
            return int(m) >= int(n) #FIXME
        else:
            raise Exception("invalid size comparison")

    def __eq__(m, n):
        if isinstance(n, natural):
            return m.val == n.val
        else:
            raise Exception("invalid size comparison")

    def __ne__(m, n):
        if isinstance(n, natural):
            return m.val != n.val
        else:
            raise Exception("invalid size comparison")

    def __int__(m):
        return int(m.val)

    def __floor__(m):
        return natural(m)

    def __ceil__(m):
        return natural(m)



class integer: ...
class integer:
    def __init__(self, val):
        if not\
            (isinstance(val, int)\
            or getattr(val, "isinteger", lambda: False)()):

            raise Exception("invalid value for integer")

        self.val = int(val) #FIXME

    def isnatural(m):
        return m >= integer(0)

    def isinteger(m) -> bool:
        return True

    def isrational(m) -> bool:
        return True

    def isreal(m) -> bool:
        return True

    def sgn(m):
        zero = integer(0)

        if m > zero: return integer(1)
        elif m == zero: return integer(0)
        elif m < zero: return integer(-1)
        else: raise Exception

    def log(m, base):
        if isinstance(base, integer):
            k = integer(0)
            while m != integer(1):
                if m%base != integer(0):
                    break
                else:
                    m //= base
                    k += integer(1)
            else:
                return k

        raise Exception("invalid log")

    @staticmethod
    def gcd(a: integer, b: integer): # euclidean algorithm
        a, b = abs(a), abs(b)
        a, b = max(a,b), min(a,b)
        while a != integer(0) and b != integer(0):
            a -= b * (a//b)
            a, b = b, a
            
        return a

    @staticmethod
    def reduce(a: integer, b: integer):
        gcd_value = integer.gcd(a, b)
        a //= gcd_value
        b //= gcd_value

        return a, b

    def __repr__(self):
        return str(self.val)

    def __pos__(m):
        return integer(m)

    def __neg__(m):
        return integer(-int(m)) #FIXME

    def __abs__(m):
        return integer(abs(int(m))) #FIXME

    def __add__(m, n):
        if isinstance(n, integer):
            return integer(int(m) + int(n)) #FIXME
        else:
            raise Exception("invalid addition")

    def __sub__(m, n):
        if isinstance(n, integer):
            return integer(int(m) - int(n)) #FIXME
        else:
            raise Exception("invalid subtraction")

    def __mul__(m, n):
        if isinstance(n, integer):
            return integer(int(m) * int(n)) #FIXME
        else:
            raise Exception("invalid multiplication")

    def __truediv__(m, n):
        if isinstance(n, integer):
            if int(m) % int(n) == integer(0): #FIXME
                return integer(int(m) // int(n)) #FIXME

        raise Exception("invalid division")

    def __floordiv__(m, n):
        if isinstance(n, integer):
            return integer(int(m) // int(n)) #FIXME

        raise Exception("invalid division")

    def __mod__(m, n):
        if isinstance(n, integer):
            return integer(int(m) % int(n)) #FIXME

        raise Exception("invalid modular")

    def __pow__(m, n):
        if isinstance(n, integer): #FIXME
            if n >= integer(0):
                return integer(int(m)**int(n)) #FIXME

        raise Exception("invalid power operation")

    def __gt__(m, n):
        if isinstance(n, integer):
            return int(m) > int(n) #FIXME
        else:
            raise Exception("invalid size comparison")
        
    def __ge__(m, n):
        if isinstance(n, integer):
            return int(m) >= int(n) #FIXME
        else:
            raise Exception("invalid size comparison")

    def __lt__(m, n):
        if isinstance(n, integer):
            return int(m) < int(n) #FIXME
        else:
            raise Exception("invalid size comparison")
        
    def __le__(m, n):
        if isinstance(n, integer):
            return int(m) <= int(n) #FIXME
        else:
            raise Exception("invalid size comparison")

    def __eq__(m, n):
        if isinstance(n, integer):
            return m.val == n.val
        else:
            raise Exception("invalid size comparison")

    def __ne__(m, n):
        if isinstance(n, integer):
            return m.val != n.val
        else:
            raise Exception("invalid size comparison")

    def __int__(self):
        return int(self.val)

    def __floor__(m):
        return integer(m)

    def __ceil__(m):
        return integer(m)



class rational:
    def __init__(self, numerator, denominator = integer(1)):
        if not isinstance(numerator, int | integer | rational):
            if getattr(numerator, "isrational", lambda: False)():
                numerator = numerator.__rational__()
            else:
                raise Exception("invalid numerator")
        if not isinstance(denominator, int | integer | rational):
            if getattr(denominator, "isrational", lambda: False)():
                denominator = denominator.__rational__()
            else:
                raise Exception("invalid denominator")

        if isinstance(numerator, int):
            numerator = integer(numerator)
        if isinstance(denominator, int):
            denominator = integer(denominator)

        if isinstance(numerator, integer) and isinstance(denominator, integer):
            pass
        elif isinstance(numerator, rational) and isinstance(denominator, rational):
            numerator, denominator = numerator.numerator*denominator.denominator, numerator.denominator*denominator.numerator
        elif isinstance(numerator, rational) and isinstance(denominator, integer):
            numerator, denominator = numerator.numerator, numerator.denominator*denominator
        elif isinstance(numerator, integer) and isinstance(denominator, rational):
            numerator, denominator = numerator*denominator.denominator, denominator.numerator



        if denominator == integer(0):
            raise ZeroDivisionError

        if numerator == integer(0):
            denominator = integer(1)

        sign = numerator.sgn()*denominator.sgn()
        numerator = abs(numerator)
        denominator = abs(denominator)

        self.numerator, self.denominator = integer.reduce(numerator, denominator)
        self.numerator *= sign

    def isnatural(p):
        return p.denominator == integer(1) and p.numerator >= integer(0)

    def isinteger(p):
        return p.denominator == integer(1)

    def isrational(p) -> bool:
        return True

    def isreal(p) -> bool:
        return True

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __pos__(p):
        return rational(p.numerator, p.denominator)

    def __neg__(p):
        return rational(-p.numerator, p.denominator)

    def __abs__(p):
        return rational(abs(p.numerator), p.denominator)

    def __add__(p, q):
        if isinstance(q, rational):
            return rational(p.numerator*q.denominator + p.denominator*q.numerator, p.denominator*q.denominator)
        else:
            raise Exception("invalid addition")

    def __sub__(p, q):
        if isinstance(q, rational):
            return rational(p.numerator*q.denominator - p.denominator*q.numerator, p.denominator*q.denominator)
        else:
            raise Exception("invalid subtraction")

    def __mul__(p, q):
        if isinstance(q, rational):
            return rational(p.numerator*q.numerator, p.denominator*q.denominator)
        else:
            raise Exception("invalid multiplication")

    def __truediv__(p, q):
        if isinstance(q, rational):
            return rational(p.numerator*q.denominator, p.denominator*q.numerator)
        else:
            raise Exception("invalid division")

    def __pow__(p, q):
        if isinstance(q, rational) and q.isinteger():
            if q >= rational(integer(0)):
                return rational(p.numerator**q.numerator, p.denominator**q.numerator)
            else:
                return rational(p.denominator**abs(q.numerator), p.numerator**abs(q.numerator))
        else:
            raise Exception("invalid power operation")

    def __gt__(p, q):
        if isinstance(q, rational):
            return p.numerator*q.denominator > p.denominator*q.numerator
        else:
            raise Exception("invalid comparison")
        
    def __ge__(p, q):
        if isinstance(q, rational):
            return p.numerator*q.denominator >= p.denominator*q.numerator
        else:
            raise Exception("invalid comparison")

    def __eq__(p, q):
        if isinstance(q, rational):
            return p.numerator*q.denominator == p.denominator*q.numerator
        else:
            raise Exception("invalid comparison")

    def __ne__(p, q):
        if isinstance(q, rational):
            return p.numerator*q.denominator != p.denominator*q.numerator
        else:
            raise Exception("invalid comparison")

    def __int__(self):
        if self.isinteger():
            return int(self.numerator)
        else:
            raise Exception("this rational is not an integer")

    def __floor__(p):
        return rational(p.numerator//p.denominator)

    def __ceil__(p):
        if p.isinteger():
            return rational(p.numerator, p.denominator)
        else:
            return rational(p.numerator//p.denominator + integer(1))



class real:
    def __init__(self, val):
        if not\
            (isinstance(val, int)\
            or getattr(val, "isreal", lambda: False)()):

            raise Exception("invalid value for real")

        if isinstance(val, int):
            val = integer(val)

        self.val = val
        self.valtype = []
        if val.isnatural():
            self.valtype.append(natural)
        if val.isinteger():
            self.valtype.append(integer)
        if val.isrational():
            self.valtype.append(rational)

    def isnatural(x):
        return natural in x.valtype

    def isinteger(x):
        return integer in x.valtype

    def isrational(x):
        return rational in x.valtype

    def isreal(x) -> bool:
        return True

    def __rational__(self):
        return rational(self.val)






