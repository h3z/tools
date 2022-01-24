from forks.all_forks import FORKS

res = [(fork.name, fork.check_harvester()) for fork in FORKS]
for i in res:
    print(i)
