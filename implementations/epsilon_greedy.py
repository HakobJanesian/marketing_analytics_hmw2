import os
import csv
import random

from interfaces.Bandit import Bandit


class EpsilonGreedy(Bandit):
    def __init__(self, p, epsilon=1.0):
        self.p = p
        self.epsilon = epsilon
        self.t = 0
        self.X = 0
        self.data = []
        self.regrets = []
   
    def __repr__(self):
        return f"EpsilonGreedy(p={self.p}, epsilon={self.epsilon})"
    
    def pull(self):
        return 1 if random.random() < self.p else 0
    
    def update(self, x):
        # self.N += 1
        # self.X = self.X + (x - self.X) / self.N
        self.data.append(x)
    
    def decay_epsilon(self):
        if self.t > 0:
            self.epsilon = 1 / self.t
    
    def experiment(self, num_trials=1000, true_best_p=None):
        for _ in range(num_trials):
            self.decay_epsilon()
            if random.random() < self.epsilon:
                reward = self.pull()
            else:
                reward = self.pull()
            self.update(reward)
            
            regret = (true_best_p - reward) if true_best_p else 0
            self.regrets.append(regret)
    
    def report(self, bandit_number, algorithm_name="EpsilonGreedy"):
        if not os.path.exists("results"):
            os.mkdir("results")
        
        subfolder_path = "results/epsilon_greedy_results"
        if not os.path.exists(subfolder_path):
            os.mkdir(subfolder_path)
        
        csv_path = os.path.join(subfolder_path, "data.csv")
        file_exists = os.path.exists(csv_path)
        
        if not file_exists:
            with open(csv_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Bandit", "Reward", "Algorithm"])
        
        cumulative_rewards = [sum(self.data[:i+1]) for i in range(len(self.data))]
        
        with open(csv_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for cum_reward in cumulative_rewards:
                writer.writerow([bandit_number, cum_reward, algorithm_name])
        
        cumulative_reward = sum(self.data)
        cumulative_regret = sum(self.regrets)
        
        return {
            "Cumulative Reward": cumulative_reward,
            "Cumulative Regret": cumulative_regret
        }
