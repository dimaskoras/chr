from main import CharsetEditor


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
