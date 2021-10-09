import subprocess
import yaml
from pathlib import Path
from subprocess import CalledProcessError
import ast


def filter_lines(res, tar):
    for line in str(res).split('\\n'):
        if tar in line:
            return line.split(':')[1].strip()


class BaseFork:
    def __init__(self, name, exec_path, work_dir, ca_path, new_address, is_harvester):
        self.name = name
        self.__exec = exec_path
        self.__work_dir = Path(work_dir)
        self.__init_ca = Path(ca_path)
        self.__isharv = is_harvester
        self.__newaddress = new_address

        # self.__check_parametes()

    def __check_parametes(self):
        try:
            subprocess.check_output([self.__exec, 'version'])
        except CalledProcessError:
            print('exec error')
        if not self.__work_dir.is_dir():
            print('work dir error')
        if self.__isharv:
            if not self.__init_ca.is_dir():
                print('ca dir error')

    def __get_wallet_status(self):
        if self.__isharv:
            return
        res = subprocess.check_output([self.__exec, 'wallet', 'show'])
        return filter_lines(res, 'Sync status:')

    def __get_fullnode_status(self):
        if self.__isharv:
            return
        res = subprocess.check_output([self.__exec, 'show', '-s'])
        return filter_lines(res, 'Current Blockchain Status:')

    def get_wallet_balance(self):
        if self.__isharv:
            return
        res = subprocess.check_output([self.__exec, 'wallet', 'show'])
        amount = filter_lines(res, '-Total Balance:')
        if amount:
            return amount.split(' ')[0]

    def get_reward_address(self):
        if self.__isharv:
            return

        with open(self.__work_dir / 'config' / 'config.yaml', 'r') as stream:
            try:
                config = yaml.safe_load(stream)
                for k in config['farmer']:
                    if 'target_address' in k:
                        return config['farmer'][k], config['pool'][k]
            except yaml.YAMLError as exc:
                print(exc)

    def fix(self):
        config_path = self.__work_dir / 'config' / 'config.yaml'
        config = ''
        with open(config_path, 'r') as stream:
            data = stream.read().replace('\n', '')
            data = data[1:-3]
            data = data.replace("''", "'")
            config = ast.literal_eval(data)
        config_path = self.__work_dir / 'config' / 'config.yaml'
        with open(config_path, 'w') as file:
            yaml.dump(config, file)

    def set_reward_address(self):
        if self.__isharv:
            return

        config_path = self.__work_dir / 'config' / 'config.yaml'
        with open(config_path, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
                for k in config['farmer']:
                    if 'target_address' in k:
                        config['farmer'][k] = self.__newaddress
                        # config['pool'][k] = self.__newaddress
                        with open(config_path, 'w') as file:
                            dest = str(config) + '__'
                            yaml.dump(dest, file)
                            return "Success"
            except yaml.YAMLError as exc:
                print(exc)
                return "Failure"

    def chia_init(self):
        res = subprocess.check_output([self.__exec, 'init'])
        print(str(res).split('\\n')[-2])

    def chia_init_c(self):
        if not self.__isharv:
            return

        res = subprocess.check_output([self.__exec, 'init', '-c'])
        print(str(res).split('\\n')[-2])

    def check_sync(self):
        if self.__isharv:
            return False
        return self.__get_wallet_status() == 'Synced' and \
               self.__get_fullnode_status() == 'Full Node Synced'

    def chia_version(self):
        res = subprocess.check_output([self.__exec, 'version'])
        return str(res).split('\\n')[0]

    def check_harvester(self):
        f_debug = str(self.__work_dir / 'log' / 'debug.log')

        process_grep = subprocess.Popen(['grep', 'Found 0', f_debug], stdout=subprocess.PIPE, shell=False)
        process_tail = subprocess.Popen(['tail', '-n', '1'], stdin=process_grep.stdout, stdout=subprocess.PIPE,
                                        shell=False)
        process_grep.stdout.close()
        return process_tail.communicate()[0]

    def restart_harvester(self):
        return subprocess.check_output([self.__exec, 'start', 'harvester', '-r'])
