<h1 align="center"> <img width="80%" src="https://www.schoolsyst.com/assets/logotype-horizontal.png"><br>Backend API  <img alt="Build status" src="https://img.shields.io/travis/com/schoolsyst/backend?label=stable%20build&style=flat-square"> </h1> </center>

## What is schoolsyst?

If you don't know, you should head over to [the main repository](http://git.schoolsyst.com/frontend), where all feature requests & bug reports are posted.
This one is strictly about the *API* schoolsyst's frontend webapp uses.

For now, this API is closed and can only be used from `*.schoolsyst.com` domains, as the only thing running all of schoolsyst is a tiny VPS.

## Great, I came from the main repo because I want to run the backend locally. How?

1. Clone the repository

```bash
git clone http://git.schoolsyst.com/backend
```

2. Create a virtual environment & activate it

```bash
python3 -m venv ./env
source env/bin/activate # On linux (bash)
. env/bin/activate.fish # On linux (fish)
.\env\Scripts\activate.bat # On windows
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Run the migrations

```bash
python3 manage.py migrate
```

5. Serve the server on port 9999

```bash
python3 manage.py runserver 9999
```

