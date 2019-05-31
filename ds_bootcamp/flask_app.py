from flask import Flask, jsonify
import os
import yaml

dir_path = os.path.dirname(os.path.realpath(__file__))


def create_app():
    app = Flask(__name__)
    
    with open(os.path.join(dir_path, 'yamls', 'dave_model.yaml')) as f:
        dave_model = yaml.load(f, Loader=yaml.SafeLoader)

    @app.route("/dave")
    def dave_hello_world():
        return "Hello, World!", 200

    @app.route("/dave_model/<submodel>/<x_1>")
    def dave_yaml_model(submodel, x_1):
        try:
            model = dave_model[submodel]
        except KeyError:
            return 'Model not found', 404
        dict_ = {'score': model['b_0'] + model['b_1'] * int(x_1)}
        return jsonify(dict_)

    return app
