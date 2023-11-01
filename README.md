# Twinoid forums archive

API and application to access a Twinoid forums archive.

## Run locally

You need [Python 3.11](https://www.python.org/downloads/release/python-3116/) to run this application. Create a virtual environment and install the requirements:

Create a virtual environment and install the requirements:

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can also use [pyenv](https://github.com/pyenv/pyenv#automatic-installer) to install Python and [poetry](https://python-poetry.org/docs/) to install dependencies if that is your thing :

If you have `make` installed, just run `make` to install and start the application.

Otherwise :

```bash
pyenv install 3.11
pyenv local 3.11
poetry install --with=dev,test
poetry shell
```

Then run the API:

```bash
cd api
uvicorn main:api --reload
```

And the application:

```bash
cd app
streamlit run main.py
```

