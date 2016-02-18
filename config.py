# CONFIG FILE WITH CONSTANTS

# Livesplit connection
HOST = "localhost"
PORT = 16834

# In network communication, time out after this time. (in seconds)
COM_TIMEOUT = 0.5

# Possible commands to send to LiveSplit
LS_COMMANDS = {
	"best_possible": "getbestpossibletime\r\n",
	"cur_split_index": "getsplitindex\r\n",
	"cur_split_name": "getcurrentsplitname\r\n"
}

# Default Window Size
DEFAULT_WINDOW = {"WIDTH": 400, "HEIGHT": 300, "TITLE": "SplitNotes"}

# Default Welcome Message
DEFAULT_MSG = "Right Click to Open Notes."

# Update time for polling livesplit and other actions (in seconds)
POLLING_TIME = 0.5

# file names and path for resources
RESOURCE_FOLDER = "resources"
ICONS = {"GREEN": "green.png", "RED": "red.png", "SETTINGS": "settings_icon.png"}
SETTINGS_FILE = "config.cfg"

# Popup menu options
MENU_OPTIONS = {
	"SINGLE": "Set Single Layout",
	"DOUBLE": "Set Double Layout",
	"LOAD": "Load Notes",
	"BIG": "Big Font",
	"SMALL": "Small Font",
	"SETTINGS": "Settings"
}

# Error messages
ERRORS = {"NOTES_EMPTY": ("Error!", "Notes empty or can't be loaded!"),
		  "FONT_SIZE": ("Error!", "Invalid Font Size!"),
		  "SERVER_PORT": ("Error!", "Invalid server port!")}

# Max file size for notes
MAX_FILE_SIZE = 1000000000  # 1 Giga-Byte

# To be added to title to alert user that timer is running
RUNNING_ALERT = "RUNNING"

# Font for notes/
# TODO FIX THIS
FONT = {"NAME": "arial", "SMALL": 12, "BIG": 16}
GUI_FONT = ("arial", 12)

# Color scheme
COLOR = {"TEXT": "black", "TEXT_BG": "ivory"}

# Files tht should be displayed and opened a notes
TEXT_FILES = [
	("Text Files", ("*.txt", "*.log", "*.asc", "*.conf", "*.cfg")),
	('All', '*')
]

# Default content of config.cfg file
DEFAULT_CONFIG = "notes=\nfont_size=12\nfont=arial\ntext_color=#FFFFFF\nbackground_color=#000000\nserver_port=16834"

# Required settings
REQUIRED_SETTINGS = ("notes",
					 "font",
					 "font_size",
					 "text_color",
					 "background_color",
					 "server_port"
					 )

# Settings window options
SETTINGS_WINDOW = {"TITLE": "Settings",
				   "WIDTH": 360,
				   "HEIGHT": 280,
				   "CANCEL": "Cancel",
				   "SAVE": "Save"}

# OPTIONS IN THE SETTINGS WINDOW
SETTINGS_OPTIONS = {"FONT": "Font",
					"FONT_SIZE": "Font Size",
					"TEXT_COLOR": "Text Color",
					"BG_COLOR": "Background Color",
					"SERVER_PORT": "LiveSplit Server port",
					"DEFAULT_SERVER_PORT": "(Default is 16834)"}

# Fonts that can be selected
AVAILABLE_FONTS = ("arial",
				   "courier new",
				   "comic sans",
				   "fixedsys",
				   "ms sans serif",
				   "ms serif",
				   "system",
				   "times new roman",
				   "verdana")
