import math_ops

print(math_ops.add(5, 3))
print(math_ops.multiply(4, 3))
print(math_ops.divide(10, 2))

from math_ops import PI, absolute, negate, power, subtract

print(subtract(10, 4))
print(power(2, 3))
print(negate(5))
print(absolute(-42))
print(PI)

import math_ops as mo

print(mo.floor_divide(17, 5))
print(mo.modulus(17, 5))

from math_ops import *

print(add(10, 20))
print(multiply(6, 7))
print(power(5, 2))