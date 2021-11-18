from flask import Flask, render_template
from redis import Redis
import docker
import json

app = Flask(__name__)

redis = Redis(host='redis', port=6379)


def data():
    client = docker.DockerClient(base_url='http://192.46.221.204:2375')

    return client

@app.route("/")
def services():
    details = data()
    final = details.nodes.list(filters={'role': 'worker'})
    list = []
    for node in final:
         dict = {}
         dict["Node shord_id"] = node.short_id
         dict["Node ID"] = node.id
         dict["Node version"] = node.version

         list.append(dict)

    name = json.dumps(list, indent = 4)
    return render_template('home.html', content=name)

@app.route('/service')
def hello():
    count = redis.incr('hits')
    details = data()
    final = details.services.list()
    list = []
    for service in final:
        dict ={}
        dict["Service Name"] = service.name
        dict["Service ID"] = service.id
        dict["Service Version"] = service.version

        list.append(dict)

    name = json.dumps(list, indent = 4)

    return render_template('index.html', count=count, content=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
