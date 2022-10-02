# from multiprocessing.connection import wait
# from flask import Flask
from flask import Flask, render_template, redirect, url_for, request
from Database.entry import *
import json



app = Flask(__name__)


@app.route("/")
def run_app():
    return render_template("/index.html")
    # return "<h1>Hello World!</h1>"

@app.route("/test", methods=['POST'])
def test():
    output = request.get_json()
    result = json.loads(output)

    c, conn = create_connection()
    create_table(c)
    insert_data(c, result['email'])
    save_session(conn)

    return result




if __name__ == '__main__':

    app.run(debug=True)
    

