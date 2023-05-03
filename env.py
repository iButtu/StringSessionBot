import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "29698700").strip()
API_HASH = os.getenv("API_HASH", "c08d5af866792c7f96e2de2b35ad5a34").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6005321257:AAFytdaPgqN8Q6ECsB9V9dQKnTGk2DB5q1M").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://yoqdgotu:D2BaXqX7e4VBZQRrLoGzevz3UqFiQPf9@lallah.db.elephantsql.com/yoqdgotu").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "solotreee")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
