from flask import Flask

from routes import (
    charset_count,
    charset_unique,
    charset_remove_duplicates,
    charset_palindromes
)


app = Flask(__name__)


app.add_url_rule("/charset_count", "charset_count", charset_count)
app.add_url_rule("/charset_unique", "charset_unique", charset_unique)
app.add_url_rule("/charset_remove_duplicates", "charset_remove_duplicates", charset_remove_duplicates)
app.add_url_rule("/charset_palindromes", "charset_palindromes", charset_palindromes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
