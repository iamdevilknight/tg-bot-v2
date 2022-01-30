# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "894f663e1e289f898208e3a26f798214"
    OWNER_ID = "598719108"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "MasterOfTG"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://moviejunction:HZ2gXX6T7NhYHjoSQBsBDWBkdmJRk8ee@dpg-c7ra8u3ru51k5psuerc0:5432/dianabot'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['cust_filters']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [254318997 18673980 83489514]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = true  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAACAgUAAxkBAAELV_RhHKkx0J7OA8dW-R54eIoIWWvBFAACkAMAAjTZ6VStsI_6u6Yx1CAE'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    BMERNU_SCUT_SRELFTI = 0

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
