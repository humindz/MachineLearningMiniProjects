from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import pickle

app = Flask(__name__)
api = Api(app)

########### Loading Vectorizer for preprocessing ###########
filename_vectorizer = 'fakeNews_vectorizer.sav'
loaded_vectorizer = pickle.load(open(filename_vectorizer, 'rb'))

########### Loading Model for predicting ###########
filename_model = 'fakeNews_model.sav'
loaded_model = pickle.load(open(filename_model, 'rb'))
############################################################

@app.route('/test', methods=['POST'])
def test():
  news_data = []
  news_data.append(request.json['news'])
  v_input_news = loaded_vectorizer.transform(news_data)

  print(v_input_news[0])
  print(loaded_model.predict(v_input_news[0]))
  return jsonify({'prediction' : loaded_model.predict(v_input_news[0])[0]})


if __name__ == "__main__":
  app.run(debug=True)