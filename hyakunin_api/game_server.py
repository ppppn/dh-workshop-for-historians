from bottle import route, run, static_file, request, template
import requests

# Answer Page Template
QUIZ_HTML = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta charset="UTF-8">
    <title>Hyakunin-Isshu Game</title>
    <script type="text/javascript">
    <!--
        function print_answer(){
            window.alert('{{second_p}}')
        }
    -->
    </script>
</head>
<body>
    <h1>Hyakunin-Isshu Quiz</h1>
    <h2>First Phrase</h2>
    <p>{{first_p}}</p>
    <p>
        <input type="button" value="Show Second Phrase"
               onclick="print_answer()">
    </p>
    <p>
        <a href="./quiz?id={{next_id}}">Next</a>
    </p>
    <p>
        <a href="../">Return to Home</a>
    </p>
</body>
</html>
'''

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


def fetch_result(id):
    url = 'http://localhost:10080/song/{id}'.format(id=id)
    res = requests.get(url)
    if res.status_code == 404:
        return None
    values = res.text.split('|')
    return {
        "id": values[0],
        "first_p": values[3],
        "second_p": values[4]
    }


@route('/')
def search_box():
    return static_file('question.html', root='html/')


# Run search
@route('/quiz')
def show_quiz():
    # Parse GET request and get song ID
    id = request.query.id
    # Connect to API server
    res_dict = fetch_result(id)
    if not res_dict:
        return NOT_FOUND_HTML
    return template(
        QUIZ_HTML,
        next_id=int(res_dict['id'])%100+1,
        first_p=res_dict['first_p'],
        second_p=res_dict['second_p']
    )


# Run the web server at http://localhost:8081
run(host='localhost', port=8081)