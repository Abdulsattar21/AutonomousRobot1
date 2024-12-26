from math import cos, sin, pi
import math

class Localization:

    def __init__(self, el, er, L):
        self.er = er
        self.el = el    
        self.L = L 

        self.wl_last_counter = 0
        self.wr_last_counter = 0


        self.x = 0
        self.y = 0
        self.theta = 0 

        self.meters_per_ticks_left =(2 * math.pi * self.el.radius)/(el.ticks_per_rev)
        self.meters_per_ticks_right =(2 * math.pi * self.er.radius)/(er.ticks_per_rev)

    def step(self):
        delta_ticks_right = (self.er.counter - self.wr_last_counter)
        delta_ticks_left = (self.el.counter - self.wl_last_counter)
        self.wl_last_counter = self.el.counter
        self.wr_last_counter = self.er.counter
        
        Dr = delta_ticks_right * self.meters_per_ticks_right
        Dl = delta_ticks_left * self.meters_per_ticks_left
        Dc = (Dr + Dl)/2

        x_dt = Dc * cos(self.theta)
        y_dt = Dc * sin(self.theta)
        theta_dt = (Dr - Dl)/self.L

        self.x = self.x + x_dt
        self.y = self.y + y_dt
        self.theta = self.theta + theta_dt

        return self.x, self.y, self.theta

    def resetPose(self):
        self.x, self.y, self.theta = 0, 0, 0

    def getPose(self): 
        return self.x, self.y, self.theta      

