from gym_smartgrid.envs import SmartGridEnv6Easy, SmartGridEnv6Hard

if __name__ == '__main__':
    # env = SmartGridEnv6Easy()
    env = SmartGridEnv6Hard()
    env.reset()
    for i in range(50000):
        env.render(sleep_time=.5)
        env.step(env.action_space.sample()) # select a random action


    # history = env.close(path='test_history.csv')
    # env.replay('test_history.csv')
