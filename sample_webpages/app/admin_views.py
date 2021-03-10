from app import apps,render_template

@apps.route("/admin")
def new_func():
    return render_template("/admin/dashboard.html")




    # href="{{ url_for('static', filename='css/style.css') }}"
