import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--repository')
parser.add_argument('--files-to-collect-path',
                    type=Path)
parser.add_argument('--destination', type=Path)
