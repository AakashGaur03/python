# >>> x = 2
# >>> y = 3
# >>> z = 4
# >>> x+y
# 5
# >>> x ** y
# 8
# >>> x + (y * z)
# 14
# >>> 40 + 2.23
# 42.23
# >>> 40 + int(2.23)
# 42
# >>> float(40) + 2.23
# 42.23
# >>> 'chat' + 'me'
# 'chatme'
# >>> x,y,z
# (2, 3, 4)
# >>> x+1,y*4
# (3, 12)
# >>> y%2
# 1
# >>> z**5
# 1024
# >>> 100**2
# 10000
# >>> 2**100
# 1267650600228229401496703205376
# >>> 2**1000
# 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

# >>> result = 1/3
# >>> result
# 0.3333333333333333
# >>> repr('chai')
# "'chai'"
# >>> str('chai')
# 'chai'
# >>> print('nice')
# nice
# >>> 1<2
# True
# >>> 
# >>> 5.0 == 5.0
# True
# >>> 4.0 != 5.0
# True
# >>> x,y,z
# (2, 3, 4)
# >>> x<y<z
# True
# >>> x<y and y<z
# True
# >>> x<y or y<z
# True
# >>> x<y or y>z
# True
# >>> x<y and y>z
# False
# >>> 1 == 2<3
# False
# >>> 1== 2 and 2<3
# False

# >>> import math
# >>> math.floor(3.5)
# 3
# >>> math.floor(3.7)
# 3
# >>> math.ceil(3.7)
# 4
# >>> math.ceil(3.1)
# 4
# >>> math.ceil(-3.1)
# -3
# >>> math.floor(-3.1)
# -4
# >>> 

# Number close to Zero
# >>> math.trunc(2.8)
# 2
# >>> math.trunc(-2.8)
# -2
# >>> 999999999999999999999999999999*2.1
# 2.1e+30
# >>> 2 + 1j
# (2+1j)
# >>> (2 + 1j) *3
# (6+3j)

# 0o for Octal
# >>> 0o20
# 16
# 0o for Hexal
# >>> 0xFF
# 0o for Binary
# 255
# >>> 0b1000
# 8
# >>> oct(64)
# '0o100'
# >>> hex(64)
# '0x40'
# >>> bin(64)
# '0b1000000'
# >>> int('64',8)
# 52
# >>> int('64',16)
# 100
# >>> int('1000',2)
# 8

# Bitwise Operator
# >>> x = 1
# >>> x<< 2
# 4
# >>> x | 2
# 3

# >>> import random
# >>> random.random()
# 0.6526083261808772
# >>> random.random()
# 0.21712190355707395
# >>> random.randint(1,100)
# 17
# >>> random.randint(1,100)
# 36
# >>> l1=['sdf','dsfsd','dfgg']
# >>> random.choice(l1)
# 'sdf'
# >>> random.choice(l1)
# 'dfgg'
# >>> random.choice(l1)
# 'dsfsd'

#  >>> random.shuffle(l1)
# >>> l1=['sdf','dsfsd','dfgg']
# >>> random.shuffle(l1)
# >>> l1
# ['sdf', 'dsfsd', 'dfgg']
# >>> random.shuffle(l1)
# >>> l1
# ['sdf', 'dsfsd', 'dfgg']
# >>> random.shuffle(l1)
# >>> l1
# ['dsfsd', 'sdf', 'dfgg']
# >>> 0.1 + 0.1 + 0.1 
# 0.30000000000000004
# >>> 0.1 + 0.1 + 0.1 - 0.3
# 5.551115123125783e-17
# >>> (0.1 + 0.1 + 0.1) - 0.3
# 5.551115123125783e-17f
# >>> from decimal import Decimal
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')
# >>> from fractions import Fraction
# >>> myFra = Fraction(2,7)
# >>> myFra
# Fraction(2, 7)

# >>> setOne = {1,2,3,4}
# >>> setOne = {1,2,3,4}
# >>> setOne 
# {1, 2, 3, 4}
# >>> setOne & {1,5,6,7}
# {1}
# >>> setOne & {1,5,6,7,3}
# {1, 3}
# >>> setOne | {1,5,6,7}
# {1, 2, 3, 4, 5, 6, 7}
# >>> setOne
# {1, 2, 3, 4}
# >>> setOne - {1,2,3,4}
# set()
# >>> type({})
# <class 'dict'>
# >>> type(setOne)
# <class 'set'>
# >>> type(True)
# <class 'bool'>
# >>> True == 1
# True
# >>> False == 0
# True
# >>> True is 1
# <python-input-102>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# >>> True + 4
# 5