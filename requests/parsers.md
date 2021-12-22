# html.parser - BeautifulSoup(markup, "html.parser")

Advantages: Batteries included, Decent speed, Lenient (as of Python 2.7.3 and 3.2.)

Disadvantages: Not very lenient (before Python 2.7.3 or 3.2.2)


# lxml - BeautifulSoup(markup, "lxml")

Advantages: Very fast, Lenient

Disadvantages: External C dependency


# html5lib - BeautifulSoup(markup, "html5lib")

Advantages: Extremely lenient, Parses pages the same way a web browser does, Creates valid HTML5

Disadvantages: Very slow, External Python dependency