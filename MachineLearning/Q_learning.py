# #
# Copyright(c) 2020 Li Luyang
# UCAS Machine learning
# date 2020 5 30 
# #

import gym
import numpy as np
from gym import wrappers

ACTION = {"LEFT":0, "DOWN":1, "RIGHT":2, "UP":3}
EPSILON = 0.2
# initial environment 
env = gym.make("FrozenLake-v0", is_slippery = False)

# decide actions
# @param (int) s: state
# @global (float) epsilon:greedy value
# @global (array) S:state set
# @output : (int) action: choose action
def action(s):
    if EPSILON <= np.random.random():
        action = np.random.randint(0,4,size=1)[0]
    else:
        action = Q[a,s]

# trianing:
def train():
    observation = env.reset()


if __name__=='__main__':
    observation = env.reset()
    env.render()
    next_state, reward, done, info = env.step(ACTION['RIGHT'])
    print(reward)
    env.render()
    env.close()
