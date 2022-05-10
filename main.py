from time import perf_counter
from decimal import Decimal, getcontext
from math import ceil, factorial as fac

start = perf_counter()

precision = 99999

getcontext().prec = precision
i = ceil(precision / 14)
c = 426880 * Decimal(10005).sqrt()
e = 1
l = 13591409
partial_sum = Decimal(l)
for k in range(1, i):
    m = fac(6*k)//(fac(3 * k)*fac(k)**3)
    l += 545140134
    e *= -262537412640768000
    partial_sum += Decimal(m * l) / e

result = str(c / partial_sum)[:-1]
print(perf_counter() - start)
print(result)