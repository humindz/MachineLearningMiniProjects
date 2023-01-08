from flask import Flask
from flask_restful import Api, Resource
import pickle

app = Flask(__name__)
api = Api(app)

text_file = open("input.txt", "r")
input_news = []
input_news.append(text_file.read())
text_file.close()

# print(input_news)

filename_vectorizer = 'fakeNews_vectorizer.sav'
loaded_vectorizer = pickle.load(open(filename_vectorizer, 'rb'))
v_input_news = loaded_vectorizer.transform(input_news)

# print(v_input_news[0])

filename_model = 'fakeNews_model.sav'
loaded_model = pickle.load(open(filename_model, 'rb'))

print(loaded_model.predict(v_input_news[0]))

# class HelloWorld(Resource):
#   def get(self):
#     return {"data":"Hello World"}

# api.add_resource(HelloWorld, "/helloworld")


# if __name__ == "__main__":
#   app.run(debug=True)