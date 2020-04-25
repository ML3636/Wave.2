a = float(input("Please print the a value where a can not equal 0"))
b = float(input("Please print the b value"))
c = float(input("Please print the c calue"))

x = (b**2) - (4*a*c)

s1 = (- b - (math.sqrt(x)))/(2*a)
s2 = (- b + (math.sqrt(x)))/(2*a)

print("solution 1 is",s1)
print("solution 2 is",s2)