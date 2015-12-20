# vim:fileencoding=utf8
from flask import Flask
# from myapp.controller.projects import projects

# Flask App
app = Flask(__name__)
app.secret_key = ''


# Module
# app.register_module(projects, url_prefix='/projects')


if __name__ == '__main__':
    app.run(debug=True, static_url_path='/static')
