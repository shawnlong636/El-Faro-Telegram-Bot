from flask import escape
from google.cloud import secretmanager
import telegram

def get_secrets() -> {str: str}:
    """Function to retrieve secrets from Google Cloud Secret manager.
    Returns:
        String Dictionary containing all secrets needed for the application
    """
    secrets = {"Telegram_API_Key": None,
            "Telegram_API_Hash": None,
            "Telegram_API_ID": None
            }

    client = secretmanager.SecretManagerServiceClient()
    project_id = "911288896089"
    key_name = f"projects/{project_id}/secrets/Telegram_API_Key/versions/latest"
    hash_name = f"projects/{project_id}/secrets/Telegram_API_Hash/versions/latest"
    id_name = key = f"projects/{project_id}/secrets/Telegram_API_ID/versions/latest"
    
    response = client.access_secret_version(name=key_name)
    secrets["Telegram_API_Key"] = response.payload.data.decode("UTF-8")

    response = client.access_secret_version(name=hash_name)
    secrets["Telegram_API_Hash"] = response.payload.data.decode("UTF-8")

    response = client.access_secret_version(name=id_name)
    secrets["Telegram_API_ID"] = response.payload.data.decode("UTF-8")

    for key, val in secrets.items():
        if val == None:
            raise Exception("Value for {key} cannot be None")
    
    return secrets

def TelegramWebhook(request):
    """HTTP Cloud Function to be called by Telegram Bot API.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using 'make_response'
    """

    secrets = get_secrets()

    bot = telegram.Bot(token=secrets["Telegram_API_Key"])

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        print(update.message)
        chat_id = update.message.chat.id

        bot.sendMessage(chat_id=chat_id, text=update.message.text)

        return "ok"

    # request_json = request.get_json(silent=True)
    # request_args = request.args

    # if request_json and 'name' in request_json:
    #     name = request_json['name']
    # elif request_args and 'name' in request_args:
    #     name = request_args['name']
    # else:
    #     name = 'World'
    
    # return f'Hello there {escape(name)}!'