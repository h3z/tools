from pathlib import Path
from forks.base import BaseFork
CA_PATH = Path('/root/cas')

FORKS_CONFIG = [
    {
        'work_dir': '/root/.spare-blockchain/mainnet',
        'exec_path': '/spare-blockchain/venv/bin/spare',
        'ca_path': CA_PATH / 'spare',
        'name': 'spare',
        'reward_address': 'spare18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfqdunfsz',
    }, {
        'work_dir': '/root/.silicoin/mainnet',
        'exec_path': '/silicoin-blockchain/venv/bin/silicoin',
        'ca_path': CA_PATH / 'silicoin',
        'name': 'silicoin',
        'reward_address': 'tsit18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfqcn838f',
    }, {
        'work_dir': '/root/.beernetwork/mainnet',
        'exec_path': '/beer-blockchain/venv/bin/beer',
        'ca_path': CA_PATH / 'beernetwork',
        'name': 'beernetwork',
        'reward_address': 'xbr18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfq9kj8ve',
    }, {
        'work_dir': '/root/.btcgreen/mainnet',
        'exec_path': '/btcgreen-blockchain/venv/bin//btcgreen',
        'ca_path': CA_PATH / 'btcgreen',
        'name': 'btcgreen',
        'reward_address': 'xbtc18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfqdwfmgm',
    }, {
        'work_dir': '/root/.greendoge/mainnet',
        'exec_path': '/greendoge-blockchain/venv/bin//greendoge',
        'ca_path': CA_PATH / 'greendoge',
        'name': 'greendoge',
        'reward_address': 'gdog15c5x68k4747r2ecn4xjwaaq2gmnhhzydhya26r0sjz70l762vujqhm5nhd',
    }, {
        'work_dir': '/root/.tad/mainnet',
        'exec_path': '/tad-blockchain/venv/bin//tad',
        'ca_path': CA_PATH / 'tad',
        'name': 'tad',
        'reward_address': 'tad18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfqx8k4we',
    }, {
        'work_dir': '/root/.cactus/mainnet',
        'exec_path': '/cactus-blockchain/venv/bin//cactus',
        'ca_path': CA_PATH / 'cactus',
        'name': 'cactus',
        'reward_address': 'cac18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfq7rceh8',
    }, {
        'work_dir': '/root/.wheat/mainnet',
        'exec_path': '/wheat-blockchain/venv/bin//wheat',
        'ca_path': CA_PATH / 'wheat',
        'name': 'wheat',
        'reward_address': 'wheat18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfqxzc7v6',
    }, {
        'work_dir': '/root/.chia/ext9',
        'exec_path': '/testnet9-blockchain/venv/bin/chia',
        'ca_path': CA_PATH / 'chia',
        'name': 'nch',
        'reward_address': 'nch18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfqhk6pwf',
    }, {
        'work_dir': '/root/.flax/mainnet',
        'exec_path': '/flax-blockchain/venv/bin//flax',
        'ca_path': CA_PATH / 'flax',
        'name': 'flax',
        'reward_address': 'xfx1g9gthge4yk7zuf7kf0q45lj0xxcgz2rsl6nm2naq73xse24v94nsewqdyh',
    }, {
        'work_dir': '/root/.apple/mainnet',
        'exec_path': '/apple-blockchain/venv/bin//apple',
        'ca_path': CA_PATH / 'apple',
        'name': 'apple',
        'reward_address': 'apple1g9gthge4yk7zuf7kf0q45lj0xxcgz2rsl6nm2naq73xse24v94nshz7g58',
    }, {
        'work_dir': '/root/.chiarose/mainnet',
        'exec_path': '/chia-rosechain/venv/bin/chia',
        'ca_path': CA_PATH / 'chiarose',
        'name': 'chiarose',
        'reward_address': 'xcr1g9gthge4yk7zuf7kf0q45lj0xxcgz2rsl6nm2naq73xse24v94ns99eql2',
    }, {
        'work_dir': '/root/.chaingreen/mainnet',
        'exec_path': '/chaingreen-blockchain/venv/bin//chaingreen',
        'ca_path': CA_PATH / 'chaingreen',
        'name': 'chaingreen',
        'reward_address': 'cgn1mhkqwfatgtj0qadqekxdfpgkhnd4mjcqmvwuwcjtmn2hw3w35mwqahprqk',
    }, {
        'work_dir': '/root/.maize/mainnet',
        'exec_path': '/maize-blockchain/venv/bin//maize',
        'ca_path': CA_PATH / 'maize',
        'name': 'maize',
        'reward_address': 'xmz18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfqyv3vpd',
    }, {
        'work_dir': '/root/.dogechia/mainnet',
        'exec_path': '/doge-chia/venv/bin//dogechia',
        'ca_path': CA_PATH / 'dogechia',
        'name': 'dogechia',
        'reward_address': 'xdg102wsz5ezp0sqrep085lwsdy6q7lfv0xrx6wnw3dqnvgh7ezrlkxsmuyx2n',
    }, {
        'work_dir': '/root/.melati/mainnet',
        'exec_path': '/melati-blockchain/venv/bin//melati',
        'ca_path': CA_PATH / 'melati',
        'name': 'melati',
        'reward_address': 'xmx1grwcl5he5aet33ag2ruxh3l98d0thes3le7l3e7wgkk44tq2hewqmetat6',
    }, {
        'work_dir': '/root/.cannabis/mainnet',
        'exec_path': '/cannabis-blockchain/venv/bin//cannabis',
        'ca_path': CA_PATH / 'cannabis',
        'name': 'cannabis',
        'reward_address': 'cans10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqmxehvp',
    }, {
        'work_dir': '/root/.covid/mainnet',
        'exec_path': '/covid-blockchain/venv/bin//covid',
        'ca_path': CA_PATH / 'covid',
        'name': 'covid',
        'reward_address': 'cov18akwyx9k4rchz6w8nsrp3tq3r3tmx9kag7t9x47rj6keq9pp9xfq54seh0',
    }, {
        'work_dir': '/root/.flora/mainnet',
        'exec_path': '/flora-blockchain/venv/bin//flora',
        'ca_path': CA_PATH / 'flora',
        'name': 'flora',
        'reward_address': 'xfl19ke6sf62j9yngxcdwg24papm9tp33gspeajlhtgpkxf3kegwz6kqsxplp5',
    }

]

FORKS = [BaseFork(c['name'], c['exec_path'], c['work_dir'], c['ca_path'], c['reward_address'], False) for c in FORKS_CONFIG]
