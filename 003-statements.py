# This module explores some very basic statements. For much more see
# https://docs.python.org/2/reference/index.html

age = 42
print "age is", age

if age > 40:
    print "Yep, you're old!"

while age > 18:
    age = age - 5
    print "age is now", age
    if age < 18:
        print "You're a minor!"
