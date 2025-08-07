import json

from flask import Flask, request, Response

from routes import (
    charset_count,
    charset_unique,
    charset_remove_duplicates,
    charset_palindromes
)


app = Flask(__name__)


def make_json_response(data):
    return Response(
        json.dumps(data, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )


@app.route("/charset_count")
def _charset_count():
    text = request.args.get("query", "")
    result = charset_count(text)
    return make_json_response(result)

@app.route("/charset_unique")
def _charset_unique():
    text = request.args.get("query", "")
    result = charset_unique(text)
    return make_json_response(result)

@app.route("/charset_remove_duplicates")
def _charset_remove_duplicates():
    text = request.args.get("query", "")
    result = charset_remove_duplicates(text)
    return make_json_response(result)

@app.route("/charset_palindromes")
def _charset_palindromes():
    text = request.args.get("query", "")
    result = charset_palindromes(text)
    return make_json_response(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
