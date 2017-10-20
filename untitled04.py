# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:58:12 2017

@author: 雨成天01
"""

import math
import matplotlib.pyplot as plt
x=0
y=1.5
z=0
v0=49.0  #初速度
θ0=(45/180)*math.pi
v_x0=v0*math.cos(θ0)
v_y0=v0*math.sin(θ0)
x_list=[0]
y_list=[1.5]
z_list=[0]
Δt=0.01
v_x=v_x0
v_y=v_y0
v_z=0.0
v=math.sqrt(v_x**2+v_y**2+v_z**2)
B2=0.0039+0.0058/(1+math.exp((v-35)/5))
g=9.8
n=0
while y>0:
    x=x+v_x*Δt
    y=y+v_y*Δt
    z=z+v_z*Δt
    θ=math.acos(math.sqrt(v_x**2+v_z**2)/ v)
    φ=math.atan(v_z/ v_x)
    v_x=v_x-B2*v*v_x*Δt+0.00041*v*math.cos(θ)*(2000/60)*2*math.pi*math.sin(φ)*Δt
    v_y=v_y-g*Δt
    v_z=v_z-0.00041*v*math.cos(θ)*(2000/60)*2*math.pi*math.cos(φ)*Δt
    v=math.sqrt(v_x**2+v_y**2+v_z**2)
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)
    n+=1
    
r=(y_list[n-1] )/(-y)
x_end=(x_list[n-1] +r*x)/(r+1)   
y_end=0
z_end=(z_list[n-1]+r*z)/(r+1)
x_list[n]=x_end
y_list[n]=y_end
z_list[n]=z_end
plt.title('x-y')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.plot(x_list,y_list,label="x-y") 
plt.legend(loc='upper right')
plt.show()
plt.title('z-y')
plt.xlabel('z(m)')
plt.ylabel('y(m)')
plt.plot(z_list,y_list,label="z-y")
plt.legend(loc='upper right')
plt.show()
plt.title('x-z')
plt.xlabel('x(m)')
plt.ylabel('z(m)')
plt.plot(x_list,z_list,label="x-z")
plt.legend(loc='upper right')
#plt.savefig('2-21.png')
plt.show()
print(z)


   
