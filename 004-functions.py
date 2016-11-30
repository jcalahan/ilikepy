# This module explores the definition and invocation of a Python function.

PI = 3.1459

def volume(h, r):
    value = PI * h * (r * r)
    return value

height = 42
radius = 2.0
vol = volume(height, radius)

print "Volume of a cylinder with height of %s and radius of %s is %s" \
      % (height, radius, vol)
