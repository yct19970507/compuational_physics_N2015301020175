# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 18:11:26 2017

@author: 雨成天01
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

dx=0.0065
T=149

class waves1:
    def _init_(self):
        
        self.x = np.linspace(0,0.65,101)
        self.y= np.zeros(101)
        for i in range(101):
            if 0<=i<=50:
                self.y[i] = 1/100*i
            else:
                self.y[i] = -1/100*i+1
        self.y[0] = 0
        self.y[-1] = 0

    def iteration(self):

        self.x = np.linspace(0,0.65,101)
        self.y_now= np.zeros(101)
        for i in range(101):
            if 0<=i<=50:
                self.y_now[i] = 1/100*i
            else:
                self.y_now[i] = -1/100*i+1
        self.y_now[0] = 0
        self.y_now[-1] = 0

        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)
        self.T=[]
        self.N=[]
        for j in range(1280):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)
            self.N.append((self.y_now[1]-self.y_now[0])/dx)
            self.T.append(0.0065/320*j)
           
                
        return self.y_now, self.T,self.N

class waves2:
    def _init_(self):
        
        self.x = np.linspace(0,0.65,101)
        self.y= np.zeros(101)
        for i in range(101):
            if 0<=i<=25:
                self.y[i] = 1/50*i
            else:
                self.y[i] = -1/150*i+2/3
        self.y[0] = 0
        self.y[-1] = 0

    def iteration(self):

        self.x = np.linspace(0,0.65,101)
        self.y_now= np.zeros(101)
        for i in range(101):
            if 0<=i<=25:
                self.y_now[i] = 1/50*i
            else:
                self.y_now[i] = -1/150*i+2/3
        self.y_now[0] = 0
        self.y_now[-1] = 0

        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)
        self.T=[]
        self.N=[]
        for j in range(1280):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)
            self.N.append((self.y_now[1]-self.y_now[0])/dx)
            self.T.append(0.0065/320*j)
           
                
        return self.y_now, self.T,self.N
        
class waves3:
    def _init_(self):
        
        self.x = np.linspace(0,0.65,101)
        self.y= np.zeros(101)
        for i in range(101):
            if 0<=i<=10:
                self.y[i] = 1/20*i
            else:
                self.y[i] = -1/180*i+5/9
        self.y[0] = 0
        self.y[-1] = 0

    def iteration(self):

        self.x = np.linspace(0,0.65,101)
        self.y_now= np.zeros(101)
        for i in range(101):
            if 0<=i<=10:
                self.y_now[i] = 1/20*i
            else:
                self.y_now[i] = -1/180*i+5/9
        self.y_now[0] = 0
        self.y_now[-1] = 0

        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)
        self.T=[]
        self.N=[]
        for j in range(1280):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)
            self.N.append((self.y_now[1]-self.y_now[0])/dx)
            self.T.append(0.0065/320*j)
           
                
        return self.y_now, self.T,self.N
        
class waves4:
    def _init_(self):
        
        self.x = np.linspace(0,0.65,101)
        self.y= np.zeros(101)
        for i in range(101):
            if 0<=i<=5:
                self.y[i] = 1/10*i
            else:
                self.y[i] = -1/190*i+10/19
        self.y[0] = 0
        self.y[-1] = 0

    def iteration(self):

        self.x = np.linspace(0,0.65,101)
        self.y_now= np.zeros(101)
        for i in range(101):
            if 0<=i<=5:
                self.y_now[i] = 1/10*i
            else:
                self.y_now[i] = -1/190*i+10/19
        self.y_now[0] = 0
        self.y_now[-1] = 0

        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)
        self.T=[]
        self.N=[]
        for j in range(1280):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)
            self.N.append((self.y_now[1]-self.y_now[0])/dx)
            self.T.append(0.0065/320*j)
           
                
        return self.y_now, self.T,self.N

plt.figure(figsize=(10,10))
plt.title('force on bridge vs time')
A = waves1()
A.iteration()
plt.subplot(221)
plt.plot(A.T,A.N,'b')
plt.xlabel('Time(s)')
plt.ylabel('bridge force(arbitrary units)')
plt.title('pluck at 1/2')
plt.xlim(0,0.02)
plt.ylim(-2,2)
plt.grid(True)
plt.show()


A = waves2()
A.iteration()
plt.subplot(222)
plt.plot(A.T,A.N,'b')
plt.xlabel('Time(s)')
plt.ylabel('bridge force(arbitrary units)')
plt.title('pluck at 1/4')
plt.xlim(0,0.02)
plt.ylim(-2,5)
plt.grid(True)
plt.show()


A = waves3()
A.iteration()
plt.subplot(223)
plt.plot(A.T,A.N,'b')
plt.xlabel('Time(s)')
plt.ylabel('bridge force(arbitrary units)')
plt.title('pluck at 1/10')
plt.xlim(0,0.02)
plt.ylim(-2,10)
plt.grid(True)
plt.show()


A = waves4()
A.iteration()
plt.subplot(224)
plt.plot(A.T,A.N,'b')
plt.xlabel('Time(s)')
plt.ylabel('bridge force(arbitrary units)')
plt.title('pluck at 1/20')
plt.xlim(0,0.02)
plt.ylim(-2,20)
plt.grid(True)
plt.show()