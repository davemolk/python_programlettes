# gunicorn


def render_template(template_name='index.html', context={}):
    html_str = ""
    with open(template_name) as f:
        # read to string
        html_str = f.read()
        # replace any context value that's in dictionary and in template
        html_str = html_str.format(**context)
    return html_str


def app(environ, start_response):
    path = environ.get("PATH_INFO") # key with url as value
    if path == '/':
        data = render_template(template_name='index.html',
        context = {'path': path})
    else:
        data = render_template(template_name='404.html',
        context = {'path': path})
    data = data.encode('utf-8') # turn to byte-string
    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])

# gunicorn server:app --reload