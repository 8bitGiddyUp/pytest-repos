# f = lambda x: 3*x+1
# print(f)
# print(f(3))

# def f(x):
#   return x(x)

# r = f(2)
# print(r)

# def f(x):
#   def g(y):
#     return x(y) --> error: undefined yet
#   return g

# r = f(2)
# print(r(3))

# the switch
# def left(a):
#   def f(b):
#     return a
#   return f

# def right(a):
#   def f(b):
#     return b
#   return f

# print(left('5v'))

# print(left('5v')('gnd'))
# print(right('5v')('gnd'))

def left2(a):
  return lambda b: a

def right2(a):
  return lambda b: b

print(left2('5v')('gnd'))
print(right2('5v')('gnd'))

l = lambda x: x
