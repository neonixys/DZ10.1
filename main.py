from flask import Flask

from utility import get_all, load_candidates, get_by_pk, get_by_skill

FILENAME = "candidates.json"
app = Flask(__name__)
data = get_all(load_candidates(FILENAME))


@app.route('/')
def index():
    str_ = '<pre>'
    for i in data:
        str_ += f"{i} \n \n \n"
    return str_


@app.route('/candidates/<int:pk>')
def get_user(pk):
    user = get_by_pk(pk, data)
    if user:
        str_ = f'<img src="{user.picture}">'
        str_ += f'</pre> {user} </pre>'
    else:
        str_ = "NOT FOUND"
        return str_

@app.route('/skills/<x>')
def get_users(x):
    users = get_by_skill(x, data)
    x = x.lower()
    if users:
        str_ = '<pre>'
        for i in data:
            str_ += f"{i} \n \n \n"
    else:
        str_ = "NOT FOUND"
    return str_

if __name__ == '__main__':
    app.run(port=5000)
