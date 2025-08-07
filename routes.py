from main import CharsetEditor

<<<<<<< HEAD

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


=======

def charset_count(text: str):
    return CharsetEditor().set_text(text).count_words()


def charset_unique(text: str):
    return CharsetEditor().set_text(text).unique()


def charset_remove_duplicates(text: str):
    result = CharsetEditor().set_text(text).remove_duplicates()
    return {"result": result}


def charset_palindromes(text: str):
    result = CharsetEditor().set_text(text).palindromes()
    return {"palindromes": result}
>>>>>>> d97cda4caa3cf172171c2c05d70d63d99f3aa4ea
