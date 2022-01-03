from unittest.mock import Mock

import main

def test_print_name():
    data = {'message': {'text': 'This is a test message',
                        'date': 1641182363,
                        'message_id': 12476345,
                        'chat': {'id': 123,
                                 'type': "not sure"}},
            'chat_id': 12342,
            'from_user': 'John',
            'update_id': 127863}

    req = Mock(method="POST", get_json=Mock(return_value=data))

    # assert main.TelegramWebhook(req) == "ok"