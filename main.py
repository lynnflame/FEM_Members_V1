"""
Code written by Lynn van der Luit
april 2026
"""

#libraries
import json
import math
import numpy as np


#read points
with open("joints0.json", "r") as file:
    joints0 = json.load(file)

#read members
with open("members.json", "r") as file:
    members0 = json.load(file)

E = 1.0 #E-modulus
A = 1.0 #area of the members

class joint:
    def __init__(self, x, y, i: int):
        self.x = x
        self.y = y
        self.i = i
        print(f"joint {i}; ({x}, {y})")

class member:
    def __init__(self, j0: joint, j1: joint, E: float=E, A: float=A):
        x0 = j0.x
        y0 = j0.y
        x1 = j1.x
        y1 = j1.y
        L = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
        K_local = E * A / L * np.matrix("1 -1; -1 1")
        c = (x1 - x0) / L
        s = (y1 - y0) / L
        T = np.matrix(f"{c} {s} 0 0; 0 0 {c} {s}")
        K = T.transpose() * K_local * T
        print(K)

joints = []
for i in range(len(joints0)):
    joints.append(joint(*joints0[i], i))

members = []
for i in range(len(members0)):
    j0, j1 = members0[i]
    members.append(member(joints[j0], joints[j1]))