# FIPL HSE Programming Course Website

## Structure

1. `source` directory contains:
   * the root `index.rst` file and other source `*.rst` files 
   * and `conf.py` for `Sphinx` configuration
2. `docs` directory contains:
   * the built website

## How to Build
1. Create virtual environment: `python -m venv venv`
2. Install the requirements with:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Check docstrings for errors:
   ```bash
   export PYTHONPATH=$(pwd):$PYTHONPATH
   python tools/docstring_linter/check_docstrings.py
   ```
4. Build the website with:
   ```bash
   export PYTHONPATH=$(pwd):$PYTHONPATH
   python tools/docs_generator/build_documentation.py
   ```

### Copy the Built Website

Copy the built website from the `build` directory into the `docs` directory.

### Add, Commit and Push 

Add, commit and push the updated `docs` directory.

### Check the Deployment

Head to the [https://fipl-hse.github.io](https://fipl-hse.github.io) to check the deployment.
