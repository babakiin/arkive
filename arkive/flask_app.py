import logging
import sys

from flask import Flask
from flask.logging import default_handler

def hello():
    return "Hello, World!"

def main():
    print("__name__ is {0}".format(__name__))
    print("{0} arguments passed.".format(len(sys.argv)))
    count = 0
    for arg in sys.argv:
        print("Argument {0}: {1}".format(count, arg))
        count += 1

    # start flask app
    log = logging.getLogger("werkzeug")
    log.setLevel(logging.ERROR)
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["ENV"] = "development"
    app.add_url_rule("/", "home", hello)
    app.run(use_reloader=False)

if __name__ == "__main__":
    main()
