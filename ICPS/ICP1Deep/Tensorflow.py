import tensorflow as tf

# Assigning values to matrix A
a = tf.constant([2,3,4,5])
# Assigning values to matrix B
b = tf.constant([3,4,5,6])
# Assigning values to matrix C
c = tf.constant([1,1,1,1])
# creating a session
session = tf.Session()
# In the question we are asked to fine the values of function (a^2 + b)* c
# Finding a^2 values and storing in variable D
d = tf.square(a)
# Adding a^2 i.e,D and B and storing in E
e= tf.add(d,b)
# Multiply (a^2 + b) i.e, E and C and storing in F
f = tf.multiply(e,c)
# Printing a*2 value
print(session.run(d))
# Printing (a*2 + b) value
print(session.run(e))
# Printing the function value which is stored in
print(session.run(f))