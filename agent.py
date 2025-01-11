import torch
import random
import numpy as np
from model import Linear_QNet, QTrainer
from collections import deque
from GameAI import Game
from matplotlib import pyplot as plt
from IPython import display

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001


def plot(scores, mean_scores):
    plt.clf()
    plt.title("TRAINING PLOT")
    plt.xlabel("NUMBER OF GAMES")
    plt.ylabel("SCORE")
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.ion()
    plt.show()
    plt.pause(.1)


class Agent:
    def __init__(self):
        self.model = Linear_QNet(8, 512, 2)
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.90  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)
        self.trainer = QTrainer(self.model, lr=LEARNING_RATE, gamma=self.gamma)
    def get_state(self, game):
        player_x, player_y = game.player.position
        player_y += game.player.height / 2
        player_velocity = game.player.fall

        if game.rectangle.rectangles:
            nearest_hole = game.rectangle.rectangles[1]
            hole_x, hole_y = nearest_hole.position
            obstacle_width, obstacle_height = nearest_hole.size
        else:
            hole_x, hole_y, obstacle_width, obstacle_height = 800, 0, 0, 0



        distance_y_top = player_y - hole_y
        distance_y_bottom = (hole_y + obstacle_height) - (player_y + game.player.height)


        state = [
            player_y < hole_y,
            player_y > hole_y + obstacle_height,
            player_velocity > 0,
            distance_y_top,
            distance_y_bottom,
            len(game.rectangle.rectangles),
            game.dead,
            game.points,
        ]
        return np.array(state, dtype=float)

    def remember(self, state, reward, action, next_state, game_over):
        self.memory.append((state, reward, action, next_state, game_over))

    def train_long_memory(self):
        if len(self.memory) == 0:
            return
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)


    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        self.epsilon = 80 - self.n_games
        final_move = [0, 0]

        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 1)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move


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

        reward, done, score = game.play(final_move)

        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.restart()
            agent.n_games += 1
            agent.train_long_memory()
            if score > best_score:
                best_score = score
                agent.model.save()
            print('GAME', agent.n_games, 'Score', score, 'current Record:', best_score)
            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            #plot(plot_scores, plot_mean_scores)


if __name__ == '__main__':
    train()
