set -ex

source venv/bin/activate
export PYTHONPATH=$(pwd)

python -m doc8 source/

rm -rf source/build/
sphinx-build -W -n -b html source/ source/build/
