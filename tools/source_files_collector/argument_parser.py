import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--repository')
parser.add_argument('--destination', type=Path)
