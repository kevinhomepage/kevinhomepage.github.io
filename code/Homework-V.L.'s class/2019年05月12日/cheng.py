n56 = 12345678901234567890123456789012345678901234567890123456
n3 = 123
import math
a = math.floor(n3 / 100) * n56
b = math.floor((n3 & 100) / 10) * 10 * n56
c = math.floor(n3 & 100 & 10) * 100 * n56
print(a + b + c)