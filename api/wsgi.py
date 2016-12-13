from api.app import app

import logging
import sys

logging.basicConfig(stream=sys.stderr)

if __name__ == "__main__":
    app.run()
