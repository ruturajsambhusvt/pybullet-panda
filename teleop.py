import time
import numpy as np
import pygame
from env import PandaEnv
from utils import JoystickControl

def teleop():
    """Minimal code to teleop panda in pybullet env using joystick"""
    
    env = PandaEnv()
    joystick = JoystickControl()
    steptime = 0.1
    start_time = time.time()
    scaling_trans = 0.1
    scaling_rot = 0.2
    env.reset()
    translation = True
    while True:
        state = env.state()

        u, start, mode, stop, X_in, Y_in = joystick.input()
        if stop:
            break
        

        xdot_h = np.zeros(6)

        if mode:
            translation = not translation

        if translation:
            xdot_h[:3] = scaling_trans * np.asarray(u)
        else:
            xdot_h[3:] = scaling_rot * np.asarray(u)

        x_pos = state['ee_position']

        xdot = xdot_h

        if x_pos[2] < 0.1 and xdot[2] < 0:
            xdot[2] = 0  


        env.step(steptime * xdot[:3])

def main():
    teleop()

if __name__ == '__main__':
    main()