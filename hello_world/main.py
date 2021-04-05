import configparser
from pathlib import Path


def main():

    ROOT_DIR = Path(__file__).parent.parent.resolve().as_posix()

    config = configparser.ConfigParser()

    config.read(f'{ROOT_DIR}/setup.cfg')

    print(config.sections())
    # print(f'ROOT_DIR={ROOT_DIR}')
    print(
        f"Your are using the verison: {config['metadata']['version']}"
        " of the script")


if __name__ == '__main__':
    exit(main())
