import flask, os
from flask.views import MethodView
from index import Index
from sign import Sign

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'), #Displays the index html template. 
                 methods=["GET"]) #This will run the GET method to show all the saved data from sql

app.add_url_rule('/sign',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)
