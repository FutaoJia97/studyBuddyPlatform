from flask import Flask
from backend.endpoint.group.group import app_group
from backend.endpoint.group_detail.group_detail import app_group_detail
from backend.endpoint.personal_info.personal_info import app_personal_info
from backend.endpoint.register.register import app_register
from backend.endpoint.login.auth import app_login

from flask_cors import CORS

# init Flask app
app = Flask(__name__)
CORS(app, supports_credentials=True)


# register blueprints
app.register_blueprint(app_group, url_prefix="/group")
app.register_blueprint(app_group_detail, url_prefix="/group_detail")
app.register_blueprint(app_personal_info, url_prefix="/personal-info")
app.register_blueprint(app_register, url_prefix="/register")
app.register_blueprint(app_login, url_prefix="/login")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
