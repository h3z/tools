from forks.all_forks import FORKS
import multiprocessing


def restart_harvester(fork):
    return (fork.name, fork.restart_harvester())


with multiprocessing.Pool(20) as p:
    res = p.map(restart_harvester, FORKS)
    for i in res:
        print(i)
