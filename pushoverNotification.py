from dotenv import dotenv_values
from pushover import Pushover # type: ignore


# Load credentials from .env file
config = dotenv_values(".env")
APP_TOKEN = config.get("PUSHOVER_API_TOKEN")
USER_KEY = config.get("PUSHOVER_USER_KEY")

po = Pushover(APP_TOKEN)
po.user(USER_KEY)

msg = po.msg("Hello, World!")

msg.set("title", "Best title ever!!!")

po.send(msg)