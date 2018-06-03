from bottle import route, run, static_file, request, template
import requests

# In this template the web server returns search result.
TEMPLATE_RESULT_HTML ='''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <title>Result - Hyakunin-Isshu Search</title>
</head>
<body>
<h1>Result - Hyakunin-Isshu Search</h1>
<table rules="all">
    <tr>
        <th>ID</th><th>Writer</th><th>1st phrase</th><th>2nd phrase</th>
    </tr>
    <tr>
        <td>{{id}}</td><td>{{writer}}</td><td>{{first_p}}</td><td>{{second_p}}</td>
    </tr>
</table>
<a href="../">Back to home</a>
</body>
</html>
'''

# The web server returns error page if the song is not found
#       (i.e. the API Server returns 404)
NOT_FOUND_HTML = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <title>Result - Hyakunin-Isshu Search</title>
</head>
<body>
<h1>Result - Hyakunin-Isshu Search</h1>
<p>Not Found</p>
<p><a href="../">Back to home</a></p>
</body>
</html>
'''


# Connect to the API server and fetch song data.
def fetch_result(id):
    url = 'http://localhost:10080/song/{id}'.format(id=id)
    res = requests.get(url)
    if res.status_code == 404:
        return None
    values = res.text.split('|')
    return {
        "id": values[0],
        "writer": values[1],
        "first_p": values[3],
        "second_p": values[-1]
    }


# https://bottlepy.org/docs/dev/tutorial.html#generating-content
# Show search box
@route('/')
def search_box():
    return static_file('searchbox.html', root='html/')


# Run search
@route('/search')
def show_result():
    # Parse GET request and get song ID
    id = request.query.id
    # Connect to API server
    res_dict = fetch_result(id)
    if not res_dict:
        return NOT_FOUND_HTML
    return template(
        TEMPLATE_RESULT_HTML,
        id=res_dict['id'],
        writer=res_dict['writer'],
        first_p=res_dict['first_p'],
        second_p=res_dict['second_p']
    )

# Run the web server at http://localhost:8080
run(host='localhost', port=8080)