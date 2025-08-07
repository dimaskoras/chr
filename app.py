import json

from flask import Flask, request, Response

from main import CharsetEditor 


app = Flask(__name__)


def make_json_response(data):
    return Response(
        json.dumps(data, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )


def get_query_text():
    return request.args.get("query", "")


@app.route("/charset_count")
def charset_count_route():
    text = get_query_text()
    result = CharsetEditor().set_text(text).count_words()
    return make_json_response(result)


@app.route("/charset_unique")
def charset_unique_route():
    text = get_query_text()
    result = CharsetEditor().set_text(text).unique()
    return make_json_response(result)


@app.route("/charset_remove_duplicates")
def charset_remove_duplicates_route():
    text = get_query_text()
    result = CharsetEditor().set_text(text).remove_duplicates()
    return make_json_response({"result": result})


@app.route("/charset_palindromes")
def charset_palindromes_route():
    text = get_query_text()
    result = CharsetEditor().set_text(text).palindromes()
    return make_json_response({"palindromes": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
