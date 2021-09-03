from forks.all_forks import FORKS_CONFIG
from forks.base import BaseFork
import multiprocessing

forks = [BaseFork(c['name'], c['exec_path'], c['work_dir'], c['ca_path'], False) for c in FORKS_CONFIG]


def check_sync(fork):
    return (fork.name, fork.check_sync())


def check_harvester(fork):
    return (fork.name, fork.check_harvester())


with multiprocessing.Pool(20) as p:
    res = p.map(check_sync, forks)
    print('sync success', [x[0] for x in (filter(lambda x: x[1], res))])
    print('sync failure', [x[0] for x in (filter(lambda x: not x[1], res))])

    res = p.map(check_harvester, forks)
    print('sync success', [x[0] for x in (filter(lambda x: x[1], res))])
    print('sync failure', [x[0] for x in (filter(lambda x: not x[1], res))])
