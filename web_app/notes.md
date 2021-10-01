
def render_template(template_name='index.html', path='/'):
    return f"<h1>Hello {path=}</h1>"


def app(environ, start_response):
    for k, v in environ.items():
        print(k, v) # request object
    path = environ.get("PATH_INFO") # key with url as value
    if path == '/':
        data = render_template(template_name='index.html', path=path)
    else:
        data = render_template(template_name='404.html', path=path)
    # data = 'Hello World!'
    # data = render_template()
    data = data.encode('utf-8') # turn to byte-string
    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])


# gunicorn server:app --reload

gunicorn calls the request object "environ"

actual path doesn't take into account the query string that is there


data = {"path": "abc", "name": "dave"}
def hello(path='/', **kwargs):
    print(path)

hello(**data)
# abc 9(value for path as key)