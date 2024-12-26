import math 

class PID:

    def __init__(self):
        self.E_d = 0
        self.E_i = 0

        # PID gains 
        self.Kp = 0.3
        self.Ki = 0 
        self.Kd = 0.003

    def step(self, x_g, y_g, x, y, theta, dt):

        u_x = x_g - x
        u_y = y_g - y
        if abs(u_x)< 0.05 and abs(u_y < 0.05): 
            # stop it 
            print("At the goal")
            return 0 

        # Angle between goal and robot
        theta_g = math.atan2(u_y, u_x)

        # error between the goal and the robot's angle
        e = theta_g - theta
        e = math.atan2(math.sin(e), math.cos(e))
        
        e_i = self.E_i + e * dt
        e_d = (e - self.E_d)/dt 

        w = self.Kp * e + self.Ki * e_i + self.Kd * e_d

        self.E_d = e_d
        self.E_i = e_i

        return w  
