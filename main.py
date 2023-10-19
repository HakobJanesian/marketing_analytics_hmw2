"""
  Run this file at first, in order to see what is it printng. Instead of the print() use the respective log level
"""
############################### LOGGER ###############################
from implementations.epsilon_greedy import EpsilonGreedy
from implementations.thompson_sampling import ThompsonSampling
from logs.logs import *
from plotting.visualization import Visualization
from plotting.comparison import comparison

def main():
    
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("MAB Application")
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    
    logger.addHandler(ch)
    
    number_of_trials = 20000
    bandit_reward = [0.1, 0.2, 0.3, 0.4]

    bandits_epsilon_greedy = [EpsilonGreedy(p=reward) for reward in bandit_reward]
    results_epsilon_greedy = {}
    
    for idx, bandit in enumerate(bandits_epsilon_greedy, start=1):
        bandit.experiment(num_trials=number_of_trials, true_best_p=max(bandit_reward))
        results_epsilon_greedy[idx] = bandit.report(bandit_number=idx)

    for bandit, result in results_epsilon_greedy.items():
        logger.info(f"Epsilon Greedy Results for Bandit {bandit} - {result}")
    
    bandits_thompson_sampling = [ThompsonSampling(p=reward) for reward in bandit_reward]
    results_thompson_sampling = {}
    
    for idx, bandit in enumerate(bandits_thompson_sampling, start=1):
        bandit.experiment(num_trials=number_of_trials, true_best_p=max(bandit_reward))
        results_thompson_sampling[idx] = bandit.report(bandit_number=idx)

    for bandit, result in results_thompson_sampling.items():
        logger.info(f"Thompson Sampling Results for Bandit {bandit} - {result}")

    visualizer = Visualization()
    
    visualizer.plot1(bandits_epsilon_greedy, algorithm_name='Epsilon-Greedy')
    visualizer.plot1(bandits_thompson_sampling, algorithm_name='Thompson Sampling')
    
    visualizer.plot2(bandits_epsilon_greedy, bandits_thompson_sampling)
    
    visualizer.plot3(bandits_epsilon_greedy, "Epsilon-Greedy")
    visualizer.plot3(bandits_thompson_sampling, "Thompson Sampling")
    
    comparison(bandits_epsilon_greedy, bandits_thompson_sampling)
    
if __name__=='__main__':
    main()
