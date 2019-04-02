import os

DATABASE_URL = os.environ.get("DATABASE_URL", None)
if not DATABASE_URL:
    DATABASE = os.environ.get("DATABASE")
    DBUSER = os.environ.get("DBUSER")
    DATABASE_URL = f'posgresql://{DATABASE}@localhost/{DBUSER}'


