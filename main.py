from flask import escape
import functions_framework
from os import environ

def hello_http(request):
    """HTTP Cloud Function.he
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using 'make_response'
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    # Telegram_API_Key = environ['Telegram_API_Key']

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return f'Hello there {escape(name)}!'