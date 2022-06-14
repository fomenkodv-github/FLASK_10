from flask import Flask
from utils import json_read

app = Flask(__name__)


@app.route('/')
def load_candidates():
    candidates: list[dict] = json_read()
    result = '<pre>'
    for candidate in candidates:
        result += f"""
          Имя кандидата - {candidate['name']}\n
          Позиция кандидата - {candidate['position']}\n
          Навыки через запятую: {candidate['skills']}\n
        """
    result += '</pre>'
    return result

@app.route('/candidates/<int:uid>')
def load_candidate(uid: int):
    candidates: list[dict] = json_read()
    result = '\n<pre>'
    for candidate in candidates:
        if uid > len(candidates):
            result += f'No such candidate #{x}, candidate number is only valid within 1 and {len(candidates)} </pre>'
            break
        if candidate.get('id') == uid:
            result += f"""
             Имя кандидата - {candidate['name']}\n
             Позиция кандидата - {candidate['position']}\n
             Навыки через запятую: {candidate['skills']}\n
            """
            result += '</pre>'
            picture = candidate.get('picture')
            picture_result: str = f'<img src="{picture}">\n{result}'
        else:
            continue
    return picture_result

@app.route('/skills/<skill>')
def load_skills(skill: str):
    candidates: list[dict] = json_read()
    result = '<pre>'
    for candidate in candidates:
        if skill.lower() in candidate['skills'].lower().replace(" ","").split(','):
            result += f"""
             Имя кандидата - {candidate['name']}\n
             Позиция кандидата - {candidate['position']}\n
             Навыки через запятую: {candidate['skills']}\n
                        """
    result += '</pre>'
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
