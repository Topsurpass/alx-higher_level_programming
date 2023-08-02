#!/usr/bin/python3

from flask import Flask, render_template
from sys import argv

app = Flask(__name__)
app.url_map.strict_slashes = False

url = argv[1]


@app.route("/")
def test_index():
    """Test html jquery and javascript"""
    return render_template(url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
