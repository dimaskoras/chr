import json

from flask import request, Response

from main import CharsetEditor

def charset_count():
    text = request.args.get("query", "")
    result = CharsetEditor().set_text(text).count_words()
    return Response(
        json.dumps(result, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

def charset_unique():
    text = request.args.get("query", "")
    result = CharsetEditor().set_text(text).unique()
    return Response(
        json.dumps(result, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

def charset_remove_duplicates():
    text = request.args.get("query", "")
    result = CharsetEditor().set_text(text).remove_duplicates()
    return Response(
        json.dumps({"result": result}, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

def charset_palindromes():
    text = request.args.get("query", "")
    result = CharsetEditor().set_text(text).palindromes()
    return Response(
        json.dumps({"palindromes": result}, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )
