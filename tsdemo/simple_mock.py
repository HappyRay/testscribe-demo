"""
Mock a dependency passed in as a parameter
"""

import json

from tsdemo.service import Service


def search_name(service: Service, keyword: str):
    name = service.search_a_name("key: " + keyword)
    d = {"name": name}
    json_str = json.dumps(d)
    return json_str
