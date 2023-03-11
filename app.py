from flask import Flask
from flask_restful import Api
from customer import Customer

application = Flask(__name__)
config = application.config
config.from_object('config')
api = Api(app=application)

api.add_resource(Customer, "/baseurl/api/v1/order-create", "/baseurl/api/v1/order", "/baseurl/api/v1/order-update")

if __name__ == "__main__":
    application.run(debug=False)