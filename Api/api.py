from flask import Flask, jsonify, abort
from flask_restful import Resource, Api
import tasks as t

app = Flask(__name__)
api = Api(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


class HelloWorld(Resource):
    def get(self):
        return {'data': 'hello world'}


api.add_resource(HelloWorld, '/')


@app.route('/hello')
def values():
    return "<h1>Hello World!</h1>"


@app.route('/todo/api/v1.0/tasks/foo/bar', methods=['GET'])
def foobar():
    return t.foo()


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify(t.getTasks())
    # return jsonify({'tasks': t.foo})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = t.getTask(task_id)
    if len(task) == 0:
        abort(404)
    return jsonify(task)


if __name__ == '__main__':
    app.run(debug=True)
