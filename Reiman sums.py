# Numerical Integration
# Reiman Sums  -  Adding small rectangles to add up the area under an integral curve


def funct_f(x):
  f= x**2
  return f
print("Enter lower limit")
lower_limit = input()
print("Enter upper limit")
upper_limit = input()
print("Enter step sizet")
step        = input()
I           = 0

x = lower_limit
while( x < upper_limit):
  area = funct_f*step
  I    = I + area
  x    = x + step

# Printing the integral 
print(I)




