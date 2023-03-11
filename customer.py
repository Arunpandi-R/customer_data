from flask_restful import Resource
from flask import Flask, make_response, jsonify
from pymongo import MongoClient
import random

from request_handle import get_meta_data_json

import config
import datetime


class Customer(Resource):

    def __init__(self):
        self.db = MongoClient(host="localhost", port=27017)

    def post(self):

        meat_data = get_meta_data_json()

        user_product_details = dict()
        total_amount = 0
        for data_product in meat_data["Product_details"]:

            total_amount = total_amount + data_product["price"] * data_product["quantity"]

        user_product_details["UserId"] = self.generate_code(code_len=10)
        user_product_details["Order_id"] = self.generate_code(code_len=6)
        user_product_details["Product_details"] = meat_data["Product_details"]
        user_product_details["Total_amount"] = total_amount
        user_product_details["Status"] = "placed"
        user_product_details["Order_data_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data_base_details = self.database()

        if data_base_details is not None:
            data_insert = data_base_details.insert_one(user_product_details)
            if data_insert is not None:
                del user_product_details["_id"]
                return make_response(jsonify({"message":"Create user data sucessfully", "result": user_product_details,
                                              "status_code": 201}, 201))
            else:
                return make_response(jsonify({"message": "data not created", "result": "",
                                              "status_code": 400}, 400))

    def get(self):
        data_base_details = self.database()
        order_data = list()
        if data_base_details is not None:
            data_fine_details = data_base_details.find()
            for i in data_fine_details:
                del i["_id"]
                order_data.append(i)
            if data_fine_details is not None:
                return make_response(jsonify({"message": "Get data successfully", "result": order_data,
                                              "status_code": 200}, 200))
            else:
                return make_response(jsonify({"message": "no user data", "result": "",

                                              "status_code": 400}, 400))
    def put(self):
        mete_data = get_meta_data_json()

        mete_data.update({"Updated_order_date_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        data_base_details = self.database()
        if data_base_details is not None:
            data_fine_details = data_base_details.update_one({"UserId": mete_data["UserId"], "Order_id": mete_data["Order_id"]}, {"$set": {"Status":mete_data["Status"], "Updated_order_date_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
            if data_fine_details is not None:
                return make_response(jsonify({"message": "Update data successfully", "result": mete_data,
                                              "status_code": 200}, 200))
            else:
                return make_response(jsonify({"message": "no user data", "result": "",

                                              "status_code": 400}, 400))


    def database(self):
        database = self.db.list_database_names()

        database_status = False
        collections_status = False

        if config.database_Name in database:
            database_status = True

        collect = None

        if database_status is False or database:
            data = self.db[config.database_Name]
            if config.collections_name in data.list_collection_names():
                collect = data[config.collections_name]
                collections_status = True
            else:
                collect = data[config.collections_name]
                collections_status = True
        if collections_status is not None:
            return collect

        else:
            return None


    def generate_code(self, code_len) -> str:
        codes = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # codes = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        lens = len(codes) - 1
        code = ''
        for i in range(code_len):
            index = random.randint(0, lens)
            code += codes[index]
        return code
