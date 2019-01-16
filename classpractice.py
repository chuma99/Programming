 
''' 2.
'''
 class Bicycle:
    def __init__(self, cadence, gear, speed):
        self.cadence = cadence
        self.gear = gear
        self.speed = speed

    def set_gear(self, newGear):
        self.gear = newGear
    def set_cadence(self, newCadence):
        self.cadence = newCadence
    def apply_brake(self, value):
        self.speed - value
    def speed_up(self):
        self.speed + value
  
''' 4. 
'''
numbers = list(numpy.arange(20, 101.5, 0.5))
total=0
for i in numbers:
    i = i*4

for i in numbers:
    total+i 
 
''' 6.
'''
from sympy import *
from sympy.geometry import *

ax = input("x-value for a: ")
ay = input("y-value for a: ")
bx = input("x-value for b: ")
by = input("y-value for b: ")
cx = input("x-value for c: ")
cy = input("y-value for c: ")

a = Point(ax, ay)
b = Point(bx, by)
c = Point(cx, cy) 

t = Triangle(a, b, c)
t.area
 
