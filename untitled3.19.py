# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:43:10 2017

@author: 雨成天01
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:51:42 2017
@author: lxwhu
"""

import pylab as pl
import math
g=9.8
l=9.8
D=0.5
q=0.5

class cp:
    def __init__(self,_theta=0.2,_w=0,_t=0,_dt=pi/1000):
        self.theta=[]
        self.theta.append(_theta)
        self.t=[]
        self.t.append(_t)
        self.w=[]
        self.w.append(_w)
        self.dt=_dt
    def cal(self,fd):
        global g,l,D,q,f1
        while(self.t[-1]<2000):
            self.w.append(self.w[-1]-g/l*sin(self.theta[-1])*self.dt-q*self.w[-1]*self.dt+fd*sin(D*self.t[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        
        return
    def plot_2d(self,fd):
        #print len(self.t) ,len(self.theta)
        plot(self.t,self.theta,lw=1,label=r'$fd=%g$'%fd)
        legend(loc='best',frameon=False)
        xlim(0,100)
        return

    def plot_phase(self,fd):
        plot(self.theta,self.w,label=r'$fd=%g$'%fd)
        legend(loc='best',frameon=False)
        xlabel(r'$\theta(radians)$')
        ylabel('w(radians/s)')
        return

  
    def cal2(self,fd):#limit theta in [-pi,pi]
        global g,l,D,q,x,y,f1
        while(self.t[-1]<800):
            self.w.append(self.w[-1]-g/l*sin(self.theta[-1])*self.dt-q*self.w[-1]*self.dt+fd*sin(D*self.t[-1])*self.dt)
            if self.theta[-1]>pi:
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt-2*pi)
            elif self.theta[-1]<-pi:
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt+2*pi)
            else :
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        x=self.theta
        y=self.w
        f1=fd

lin=[0.5,0.8,1.2]#fd=lin
for i in range(len(lin)):
    a=cp()
    a.cal2(lin[i])
    a.plot_2d(lin[i])
title(r'$\theta$ versus time')
xlabel('time(s)')
ylabel('r$\theta$(radians)')
show()