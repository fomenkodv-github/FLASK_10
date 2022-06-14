import json


def json_read(file="candidates.json") -> list[dict]:
    with open(file,encoding='utf-8') as f:
        json_content = json.loads(f.read())
    return json_content
