import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--repositories-to-collect-path',
                    type=Path)
parser.add_argument('--destination', type=Path)
