import matplotlib.pyplot as plt
import numpy as np


def comparison(bandits_egreedy, bandits_thompson):
    """
    Compare the performances of Epsilon-Greedy and Thompson Sampling visually using bar plot.
    """
    plt.figure(figsize=(14, 6))
    
    total_rewards_egreedy = sum([sum(bandit.data) for bandit in bandits_egreedy])
    total_rewards_thompson = sum([sum(bandit.data) for bandit in bandits_thompson])
    
    total_regrets_egreedy = sum([sum(bandit.regrets) for bandit in bandits_egreedy])
    total_regrets_thompson = sum([sum(bandit.regrets) for bandit in bandits_thompson])
    
    labels = ['Epsilon-Greedy', 'Thompson Sampling']
    rewards = [total_rewards_egreedy, total_rewards_thompson]
    regrets = [total_regrets_egreedy, total_regrets_thompson]
    
    width = 0.35
    x = np.arange(len(labels))
    
    rects1 = plt.bar(x - width/2, rewards, width, label='Rewards', color='blue')
    rects2 = plt.bar(x + width/2, regrets, width, label='Regrets', color='red')

    plt.ylabel('Scores')
    plt.title('Total Rewards and Regrets by Algorithm')
    plt.xticks(x, labels)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
