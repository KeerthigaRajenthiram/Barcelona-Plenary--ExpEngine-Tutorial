from eexp_engine import client
import eexp_config

if __name__ == '__main__':
    exp_name = 'Example_main'
    client.run(__file__, exp_name, eexp_config)
