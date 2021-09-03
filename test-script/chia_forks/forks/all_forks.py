from pathlib import Path

CA_PATH = Path('/root/cas')

FORKS_CONFIG = [
    {
        'work_dir': '/root/.spare-blockchain/mainnet',
        'exec_path': '/spare-blockchain/venv/bin/spare',
        'ca_path': CA_PATH / 'spare',
        'name': 'spare',
        'reward_address': 'spare10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwquhnttj',
    }, {
        'work_dir': '/root/.silicoin/mainnet',
        'exec_path': '/silicoin-blockchain/venv/bin/silicoin',
        'ca_path': CA_PATH / 'silicoin',
        'name': 'silicoin',
        'reward_address': 'tsit10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqfc8nue',
    }, {
        'work_dir': '/root/.beernetwork/mainnet',
        'exec_path': '/beer-blockchain/venv/bin/beer',
        'ca_path': CA_PATH / 'beernetwork',
        'name': 'beernetwork',
        'reward_address': 'xbr10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwq5aj9hf',
    }, {
        'work_dir': '/root/.btcgreen/mainnet',
        'exec_path': '/btcgreen-blockchain/venv/bin//btcgreen',
        'ca_path': CA_PATH / 'btcgreen',
        'name': 'btcgreen',
        'reward_address': 'xbtc10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqu9fent',
    }, {
        'work_dir': '/root/.greendoge/mainnet',
        'exec_path': '/greendoge-blockchain/venv/bin//greendoge',
        'ca_path': CA_PATH / 'greendoge',
        'name': 'greendoge',
        'reward_address': 'gdog10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqzae3th',
    }, {
        'work_dir': '/root/.tad/mainnet',
        'exec_path': '/tad-blockchain/venv/bin//tad',
        'ca_path': CA_PATH / 'tad',
        'name': 'tad',
        'reward_address': 'tad10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqhvkh4f',
    }, {
        'work_dir': '/root/.cactus/mainnet',
        'exec_path': '/cactus-blockchain/venv/bin//cactus',
        'ca_path': CA_PATH / 'cactus',
        'name': 'cactus',
        'reward_address': 'cac10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwq0gcmvh',
    }, {
        'work_dir': '/root/.wheat/mainnet',
        'exec_path': '/wheat-blockchain/venv/bin//wheat',
        'ca_path': CA_PATH / 'wheat',
        'name': 'wheat',
        'reward_address': 'wheat10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqhfcuh2',
    }, {
        'work_dir': '/root/.chia/ext9',
        'exec_path': '/testnet9-blockchain/venv/bin/chia',
        'ca_path': CA_PATH / 'chia',
        'name': 'nch',
        'reward_address': 'nch10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqxa6r4e',
    }, {
        'work_dir': '/root/.flax/mainnet',
        'exec_path': '/flax-blockchain/venv/bin//flax',
        'ca_path': CA_PATH / 'flax',
        'name': 'flax',
        'reward_address': 'xfx10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqf243cl',
    }, {
        'work_dir': '/root/.apple/mainnet',
        'exec_path': '/apple-blockchain/venv/bin//apple',
        'ca_path': CA_PATH / 'apple',
        'name': 'apple',
        'reward_address': 'apple10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwq8xt5g0',
    }, {
        'work_dir': '/root/.chiarose/mainnet',
        'exec_path': '/chia-rosechain/venv/bin/chia',
        'ca_path': CA_PATH / 'chiarose',
        'name': 'chiarose',
        'reward_address': 'xcr10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwq4pvurz',
    }, {
        'work_dir': '/root/.chaingreen/mainnet',
        'exec_path': '/chaingreen-blockchain/venv/bin//chaingreen',
        'ca_path': CA_PATH / 'chaingreen',
        'name': 'chaingreen',
        'reward_address': 'cgn10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqlkp0rl',
    }, {
        'work_dir': '/root/.maize/mainnet',
        'exec_path': '/maize-blockchain/venv/bin//maize',
        'ca_path': CA_PATH / 'maize',
        'name': 'maize',
        'reward_address': 'xmz10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwq483w6a',
    }, {
        'work_dir': '/root/.dogechia/mainnet',
        'exec_path': '/doge-chia/venv/bin//dogechia',
        'ca_path': CA_PATH / 'dogechia',
        'name': 'dogechia',
        'reward_address': 'xdg10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqkaujnt',
    }, {
        'work_dir': '/root/.melati/mainnet',
        'exec_path': '/melati-blockchain/venv/bin//melati',
        'ca_path': CA_PATH / 'melati',
        'name': 'melati',
        'reward_address': 'xmx10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqz3cyfg',
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
        'reward_address': 'cov10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwq97smvl',
    }, {
        'work_dir': '/root/.flora/mainnet',
        'exec_path': '/flora-blockchain/venv/bin//flora',
        'ca_path': CA_PATH / 'flora',
        'name': 'flora',
        'reward_address': 'xfl10gccvkafd92mhp28pqfpxj736xplw62kk5mugryz4rc5c84mnmwqjma8zs',
    }

]
