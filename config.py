import os

API_ID = API_ID = 24932120

API_HASH = os.environ.get("API_HASH", "b16b8704b5c839ed24f4ed5824978a3b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7110652733:AAHLd0OCRl17j7WDqmnLoWzEqmv3CzcWQrI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5713332230))

LOG = -1002054181760

try:
    ADMINS=[6988460039]
    for x in (os.environ.get("ADMINS", "6988460039").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


