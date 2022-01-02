from unittest.mock import Mock

import main

def test_print_name():
    name = 'test_name'
    data = {'name': name}
    req = Mock(get_json=Mock(return_value=data), args=data)

    assert main.hello_http(req) == f'Hello there {name}!'