from .config import config

from flask import request, redirect
from requests.utils import quote
from CTFd.utils.decorators import authed_only
from CTFd.utils.user import get_current_user
import hmac

def get_state_secret(app, user):
    return hmac.new(
        app.config['DISCORD_AUTH_SECRET'].encode('utf8'),
        user.id.to_bytes(8, 'big'),
        'sha256'
    ).hexdigest()

def load(app):
    config(app)

    @app.route("/writeups", methods=['GET'])
    @authed_only
    def writeups():
        user = get_current_user()
        return redirect(app.config['WRITEUPS_FORM'].format(str(user.id) + "," + get_state_secret(app, user)))
