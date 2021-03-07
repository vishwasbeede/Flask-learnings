from app import apps

@apps.route("/about")
def names():
    return "Hell world 123"

@apps.route("/index")
def names1():
    return "<a>Hello 123</a>"
