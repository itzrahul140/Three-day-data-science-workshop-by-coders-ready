# -*- coding: utf-8 -*-
"""Workshop class 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_5z0S4FjSQcR3PgVTcxyJG5gdK8tb_wN
"""

from google.colab import drive
drive.mount('/content/drive')

#comments
a = 4
a

#this is a command to assign values to the variables
#a = 4
b = 4  # here 4 value is assigned to the variable b
...
c = 6 
c = 45
d = 56
...
e = 9

# K = KEYWORDS
#def
#None
#True
#False

#I = Identifiers

a = 4
b = 4.5
c = 'coders'
d = 3 + 5j
e = 5**3
f = 9/2
g = 9//2 
h = None

d.real

d.imag

True + False

f

g

a + b

a = 4
b = 8

if a < 6 and a > 9:
  print('Rahul')

food = 'pasta'

if food is None:
  print('Just in some time, let the class finish')
else:
  print('Here, is', food)

age = 25
if age < 20:
  print('you might be right')
elif 21<age<23:
    print('age will definetly lie between this range')
else:
  print("I Dushyant verify that my age is:", age)

for Rahul in [0, 1, 2, 3]:
  print(Rahul**2)

for i in range(4):
  print(i**2)

for i in range(-3,4):
  print(i**2)

n = []
sq = []
cb = []

for i in range(20):
  a = i
  b = i**2
  c = i**3

  n.append(a)
  sq.append(b)
  cb.append(c)

n

sq

cb

import matplotlib.pyplot as plt
plt.plot(n,sq, '.-', n,cb,'*-')
plt.show()

