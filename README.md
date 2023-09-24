# FIPL HSE Programming Course Website

## Structure

1. `source` directory contains:
   * the root `index.rst` file and other source `*.rst` files 
   * and `conf.py` for `Sphinx` configuration
2. `docs` directory contains:
   * the built website

## How to Build

### Install Requirements

Install the requirements with:
```bash
python3 -m pip install -r requirements.txt
```

### Build API Pages for the Labs

```bash
python3 docs_generator/generate.py
```

**NOTE**: This should be done prior building of the project.

### Build Website

Build the website with:

1. Fool-proof(tm) script:
   ```bash
   ./build_html.sh
   ```

2. Manually
   ```bash
   sphinx-build -b html source build
   ```

where:
* `source` is the directory with the `*.rst` files
* `build` is the directory where the built website will be stored

### Copy the Built Website

Copy the built website from the `build` directory into the `docs` directory.

### Add, Commit and Push 

Add, commit and push the updated `docs` directory.

### Check the Deployment

Head to the [https://fipl-hse.github.io](https://fipl-hse.github.io) to check the deployment.
