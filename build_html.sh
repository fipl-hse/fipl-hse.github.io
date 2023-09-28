set -ex

BUILD_DIR=source/build

if [[ -d ${BUILD_DIR} ]]; then
    echo "Removing ${BUILD_DIR}"
    rm -rf ${BUILD_DIR}
fi

mkdir -p ${BUILD_DIR}

source venv/bin/activate

python docs_generator/generate.py

sphinx-build -b html source ${BUILD_DIR}
sphinx-build -b docx source ${BUILD_DIR}
