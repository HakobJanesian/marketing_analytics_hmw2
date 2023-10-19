import matplotlib.pyplot as plt
import seaborn as sns


class Visualization:

    def plot1(self, data, algorithm_name="Algo"):
        trial_points = [100, 500, 1000, 1500, 2000]
        colors = ['blue', 'green', 'red', 'purple']

        fig, axes = plt.subplots(nrows=len(trial_points), figsize=(10, 15))

        for i, trials in enumerate(trial_points):
            for j, bandit in enumerate(data):
                sns.kdeplot(bandit.data[:trials], ax=axes[i], color=colors[j], label=f'Bandit {j + 1}')
                axes[i].set_title(f'{algorithm_name} Learning Process: Distribution after {trials} trials')
                axes[i].set_xlabel('Reward')
                axes[i].set_ylabel('Density')
                axes[i].legend(loc='upper right', fontsize='small')

            plt.tight_layout()
            plt.subplots_adjust(hspace=0.9)
        plt.show()

    
    def plot2(self, bandits_egreedy, bandits_thompson):
        
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))
        
        # Cumulative Rewards Comparison
        for idx, (bandit_eg, bandit_ts) in enumerate(zip(bandits_egreedy, bandits_thompson), start=1):
            cumulative_rewards_eg = [sum(bandit_eg.data[:i+1]) for i in range(len(bandit_eg.data))]
            cumulative_rewards_ts = [sum(bandit_ts.data[:i+1]) for i in range(len(bandit_ts.data))]
            
            axes[0].plot(cumulative_rewards_eg, label=f"E-Greedy Bandit {idx}")
            axes[0].plot(cumulative_rewards_ts, label=f"Thompson Sampling Bandit {idx}", linestyle='dashed')
        
        # Cumulative Regrets Comparison
        for idx, (bandit_eg, bandit_ts) in enumerate(zip(bandits_egreedy, bandits_thompson), start=1):
            cumulative_regrets_eg = [sum(bandit_eg.regrets[:i+1]) for i in range(len(bandit_eg.regrets))]
            cumulative_regrets_ts = [sum(bandit_ts.regrets[:i+1]) for i in range(len(bandit_ts.regrets))]
            
            axes[1].plot(cumulative_regrets_eg, label=f"E-Greedy Bandit {idx}")
            axes[1].plot(cumulative_regrets_ts, label=f"Thompson Sampling Bandit {idx}", linestyle='dashed')
        
        axes[0].set_title("Comparison of Cumulative Rewards")
        axes[0].set_xlabel("Trials")
        axes[0].set_ylabel("Cumulative Rewards")
        axes[0].legend()
        
        axes[1].set_title("Comparison of Cumulative Regrets")
        axes[1].set_xlabel("Trials")
        axes[1].set_ylabel("Cumulative Regrets")
        axes[1].legend()
        
        plt.tight_layout()
        plt.show()

    def plot3(self, bandits, algorithm_name):

        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))
        
        for idx, bandit in enumerate(bandits, start=1):
            cumulative_rewards = [sum(bandit.data[:i+1]) for i in range(len(bandit.data))]
            axes[0].plot(cumulative_rewards, label=f"Bandit {idx}")
            axes[1].plot(cumulative_rewards, label=f"Bandit {idx}")
        
        axes[0].set_title(f"{algorithm_name} - Cumulative Rewards (Linear Scale)")
        axes[0].set_xlabel("Trials")
        axes[0].set_ylabel("Cumulative Rewards")
        axes[0].legend()
        
        axes[1].set_title(f"{algorithm_name} - Cumulative Rewards (Log Scale)")
        axes[1].set_xlabel("Trials")
        axes[1].set_ylabel("Cumulative Rewards")
        axes[1].set_yscale("log")
        axes[1].legend()
        
        plt.tight_layout()
        plt.show()