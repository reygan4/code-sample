import cmath

a = float(raw_input('Enter a: '))
b = float(raw_input('Enter b: '))
c = float(raw_input('Enter c: '))
print "Equation is ", a,"x^2 + ", b,"x + ", c   
d = b**2 - (4*a*c)
s1 = (-b + cmath.sqrt(d))/(2*a)
s2 = (-b - cmath.sqrt(d))/(2*a)
print  "The square roots are ", s1, " and ", s2
