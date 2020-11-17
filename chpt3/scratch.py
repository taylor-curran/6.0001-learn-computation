# Find the Cube Root of a Perfect Cube
# Return message if there is nothing.
x = int(input('Enter an integer: '))
ans = 0 
# The while loop achieves iteration.
while ans**3 < abs(x):
  ans = ans + 1 

# Ok now Ans is == Cube Root of x
# Orrrr it's greater than the cube root.
if ans**3 != abs(x):
  print(x, "is not a perfect cube")
else:
  if x < 0:
    ans = -ans
  print('Cube root of', x, 'is', ans)

  