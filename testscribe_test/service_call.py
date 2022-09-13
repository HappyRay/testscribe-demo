import json

from testscribe_test.service import Service


def gen_name(service: Service, keyword: str, start_number: int):
    name = service.search_a_name("key: " + keyword)
    num = service.search_a_number(start_number)
    num2 = service.search_a_number(start_number + 1)
    d = {"name": name, "number": num + num2}
    json_str = json.dumps(d)
    return json_str
