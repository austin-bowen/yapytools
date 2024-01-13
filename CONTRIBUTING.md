# Contributing

## Setup

```bash
# Clone the repo
git clone https://github.com/austin-bowen/yapytools.git
cd yapytools

# Setup virtual env
python3 -m venv venv
. venv/bin/activate

# Install dependencies
pip install --editable .[all]

# Run tests and generate coverage report
invoke test cov
```

## Running Tasks

Tasks like running tests, building and uploading artifacts to PyPI, etc.
are run using the `invoke <task>` command. Run `invoke -l` to list all
available tasks.

## Publishing to PyPI

1. Create `.pypirc` and `.pypirc-test` files like so:
   ```
   [pypi]
     username = __token__
     password = <token>
   ```
2. `invoke build` to create new distribution files in `dist/`.
3. `invoke publish` to publish dist files to [test.pypi.org](https://test.pypi.org).
4. `invoke publish --no-test` to publish dist files to [pypi.org](https://pypi.org).
