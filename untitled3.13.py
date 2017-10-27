# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:47:33 2017

@author: 雨成天01
"""

import pylab as pl
import math
class pendulum:
    def __init__(self, time_step=0.04, g=9.8, l=9.8, damp_coefficient=0.5, force=0.5, initial_theta_1=0.2, initial_theta_2=0.201, initial_time=0, w=0):
        self.l=l
        self.dt=time_step
        self.theta_1=[initial_theta_1]
        self.theta_2=[initial_theta_2]
        self.t=[initial_time]
        self.w_1=[w]
        self.w_2=[w]
        self.g=g
        self.q=damp_coefficient
        self.f=force
        self.omiga=2/3
        self.log_d_theta=[math.log(abs(0.201-0.2))]
    def run(self):
        for i in range(2000): 
            self.w_1.append(self.w_1[i]-((self.g/self.l)*math.sin(self.theta_1[i])+self.q*self.w_1[i]-self.f*math.sin(self.omiga*self.t[i]))*self.dt)
            self.theta_1.append(self.theta_1[i]+self.w_1[i + 1]*self.dt)
            if self.theta_1[i+1] > math.pi:
                self.theta_1[i+1] = self.theta_1[i+1] -2 * math.pi
            elif self.theta_1[i+1] < -math.pi:
                    self.theta_1[i+1] = self.theta_1[i+1] +2 * math.pi
            else:
                pass
            self.w_2.append(self.w_2[i]-((self.g/self.l)*math.sin(self.theta_2[i])+self.q*self.w_2[i]-self.f*math.sin(self.omiga*self.t[i]))*self.dt)
            self.theta_2.append(self.theta_2[i]+self.w_2[i + 1]*self.dt)
            if self.theta_2[i+1] > math.pi:
                self.theta_2[i+1] = self.theta_2[i+1] -2 * math.pi
            elif self.theta_2[i+1] < -math.pi:
                    self.theta_2[i+1] = self.theta_2[i+1] +2 * math.pi
            else:
                pass
            self.t.append(self.t[i]+self.dt)
            self.log_d_theta.append(math.log(abs(self.theta_1[i+1]-self.theta_2[i+1])))
    def show_results(self):
        pl.plot(self.t, self.log_d_theta)
        pl.title('$\Delta$$\Theta$ versue time')
        pl.xlabel('time($s$)')
        pl.ylabel('$\Delta$$\Theta$($radians$)')
        pl.text(self.t[1000], self.log_d_theta[1200],'$q2$ = '+str(self.q))
        pl.show()
