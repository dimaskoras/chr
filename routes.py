import json

from flask import request, Response

from main import CharsetEditor


class CharsetEd:
    def __init__(self):
        self.text = request.args.get("query", "")
        self.editor = CharsetEditor().set_text(self.text)


    def get_result(self, method_name):
        method = getattr(self.editor, method_name)
        return method()


    def json_response(self, data):
        return Response(
            json.dumps(data, ensure_ascii=False),
            content_type="application/json; charset=utf-8"
        )


def charset_count():
    handler = CharsetEd()
    result = handler.get_result("count_words")
    return handler.json_response(result)


def charset_unique():
    handler = CharsetEd()
    result = handler.get_result("unique")
    return handler.json_response(result)


def charset_remove_duplicates():
    handler = CharsetEd()
    result = handler.get_result("remove_duplicates")
    return handler.json_response({"result": result})


def charset_palindromes():
    handler = CharsetEd()
    result = handler.get_result("palindromes")
    return handler.json_response({"palindromes": result})



