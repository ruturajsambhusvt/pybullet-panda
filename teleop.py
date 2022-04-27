import time
import numpy as np
import pygame
from env import PandaEnv
from utils import JoystickControl

def teleop():
    """Minimal code to teleop panda in pybullet env using joystick"""
    
    env = PandaEnv()
    joystick = JoystickControl()
    quit = False
    steptime = 0.1
    start_time = time.time()
    trans_scaling = 1.0
    rot_scaling = 2.0

    env.reset()
    while not quit:
        axes, start, mode, stop = joystick.getInput()

        if stop:
            quit = True
            env.close()

        xdot = np.zeros(6)

        if mode:
            xdot[:3] = trans_scaling * np.array(axes)
        else:
            xdot[3:] = rot_scaling * np.array(axes)

        print(xdot)

        env.step(xdot)

def main():
    teleop()

if __name__ == '__main__':
    main()