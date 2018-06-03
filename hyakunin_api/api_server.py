from bottle import route, run, abort
import sqlite3


# In this format the API server returns results
RETURN_FORMAT = '''{id}|{writer}|{writer_title}|{first_phrase}|{second_phrase}'''

# Create connection to SQLite3 database files
# https://docs.python.jp/3/library/sqlite3.html
conn = sqlite3.connect('database/hyakunin.db')


# Request Routing
# https://bottlepy.org/docs/dev/tutorial.html#request-routing

# Hello page
@route('/')
def hone():
    return 'This is Hyakunin-Isshu API Server!'


# Song API
# https://bottlepy.org/docs/dev/tutorial.html#generating-content
@route('/song/<id>')
def find_song(id):
    # Return status code 404 if id is not number.
    if not id.isdigit():
        abort(404, 'Not Found')
    id = int(id)
    # Return status code 404 also if id is grater than 100 or less than 1.
    if id > 100 or id < 1:
        abort(404, 'Not Found')

    # Create cursor
    c = conn.cursor()

    # Execute SQL to fetch song data.
    # https://www.sqlite.org/lang_select.html
    c.execute("SELECT id, writer, writer_title, first_phrase, second_phrase "
              "FROM songs WHERE id "
              "= %d" % id)
    result = c.fetchall()[0]
    return RETURN_FORMAT.format(
        id=result[0],
        writer=result[1],
        writer_title=result[2],
        first_phrase=result[3],
        second_phrase=result[4]
    )


# Run API server at http://localhost:10080
run(host='localhost', port=10080)