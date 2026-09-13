set -ex

source venv/bin/activate
export PYTHONPATH=$(pwd)

rm -rf source/build/
sphinx-build -W -n -b html source/ source/build/
