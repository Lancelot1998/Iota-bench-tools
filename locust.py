# -*- coding: utf-8 -*-
"""
    Locust Shell (API)
    ~~~~~~~~

    :author: Jason Liu
"""

from flask import Flask, request
import os

app = Flask(__name__)
chainbase_address = None


@app.route("/node", methods=['GET', 'POST'])
def hello():
    os.system("node trans.js")
    return 'hello'


@app.route("/transaction", methods=['GET', 'POST'])
def transaction():
    os.system("node trans.js")
    return 'right'


if __name__ == "__main__":
    app.run()
