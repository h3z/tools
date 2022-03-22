from forks.all_forks import FORKS

res = [(fork.name, fork.set_reward_address()) for fork in FORKS]
for i in res:
    print(i)
