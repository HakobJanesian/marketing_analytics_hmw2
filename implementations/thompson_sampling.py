import os
import csv
import random
from interfaces.Bandit import Bandit


class ThompsonSampling(Bandit):
    def __init__(self, p):
        self.p = p
        self.alpha = 1
        self.beta = 1
        self.data = []
        self.regrets = []
    
    def __repr__(self):
        return f"ThompsonSampling(p={self.p}, alpha={self.alpha}, beta={self.beta})"
    
    def pull(self):
        return 1 if random.random() < self.p else 0
    
    def update(self, x):
        if x == 1:
            self.alpha += 1
        else:
            self.beta += 1
        self.data.append(x)
    
    def experiment(self, num_trials=1000, true_best_p=None):
        for _ in range(num_trials):
            # Thompson sampling step
            sample = random.betavariate(self.alpha, self.beta)
            if sample > 0.1:  # Arbitrary threshold, can be adjusted
                reward = self.pull()
                self.update(reward)
            else:
                reward = 0
                
            regret = (true_best_p - reward) if true_best_p else 0
            self.regrets.append(regret)
    
    def report(self, bandit_number, algorithm_name="ThompsonSampling"):
        if not os.path.exists("results"):
            os.mkdir("results")
        
        subfolder_path = "results/thompson_sampling_results"
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
