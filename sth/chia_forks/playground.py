from forks.all_forks import FORKS
import multiprocessing


def check_sync(fork):
    return (fork.name, fork.check_sync())


def check_harvester(fork):
    return (fork.name, fork.check_harvester())


def get_balance(fork):
    return (fork.name, fork.get_wallet_balance())


with multiprocessing.Pool(20) as p:
    res = p.map(check_sync, FORKS)
    print('sync success', [x[0] for x in (filter(lambda x: x[1], res))])
    print('sync failure', [x[0] for x in (filter(lambda x: not x[1], res))])

    res = p.map(check_harvester, FORKS)
    print('sync success', [x[0] for x in (filter(lambda x: x[1], res))])
    print('sync failure', [x[0] for x in (filter(lambda x: not x[1], res))])

    res = p.map(get_balance, FORKS)
    print(res)
