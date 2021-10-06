# from flask import Flask, escape, request, render_template
import flask
import datetime
import platform
import os

app = flask.Flask(__name__)


@app.route('/')
def hello():
    name = flask.request.args.get("name", "Capstone Project")
    time = datetime.datetime.now()
    python_version = platform.python_version()
    aws_platform = os.environ.get('PLATFORM', 'Amazon Web Services')
    pod_name = os.environ.get('POD_NAME', 'NOT FOUND')
    node_name = os.environ.get('NODE_NAME', 'NOT FOUND')
    pod_namespace = os.environ.get('POD_NAMESPACE', 'NOT FOUND')
    return flask.render_template('hello.html',
                                 platform=aws_platform,
                                 flask_version=flask.__version__,
                                 python_version=python_version,
                                 flask_url='https://palletsprojects.com/p/flask/',
                                 time=time,
                                 name=name,
                                 pod_name=pod_name,
                                 node_name=node_name,
                                 pod_namespace=pod_namespace)


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
