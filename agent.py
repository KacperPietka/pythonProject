import torch
import random
import numpy as np
#from model import Linear_QNet, QTrainer
from collections import deque
from Game import Game

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001


class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 #random
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)


    def get_state(self, game):
        pass

    def remember(self, state, reward, action, next_state, game_over):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self):
        pass

    def get_action(self, state):
        pass


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    best_score = 0
    agent = Agent()
    game = Game()
    while True:
        state_old = agent.get_state(game)

        final_move = agent.get_action(state_old)

        reward,done,score = game.game_loop(final_move)

        state_new = agent.get_state(game)

if __name__ == '__main__':
    train()
