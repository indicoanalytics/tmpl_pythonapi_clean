from flask import make_response

def setup():
    print("setup")
    make_response()

def after_request(response):
    print("after_request")
    print(response)
    make_response()

def process_response(response):
    print("process_response")
    print(response)
    make_response()