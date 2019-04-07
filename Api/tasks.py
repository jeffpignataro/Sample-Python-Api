import json


def foo():
    return 'bar'


def getData():
    with open('./Data/tasks.json', "r") as jsonFile:
        data = json.load(jsonFile)
        return data


def getTasks():
    return getData()
    # return jsonify({'tasks': t.foo})


def getTask(id):
    data = getData()
    task = [task for task in data if task['id'] == id]
    return task
