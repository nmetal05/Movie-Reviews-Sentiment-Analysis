from flask import Flask,render_template,request
import joblib
from preprocessing import preprocess


app = Flask(__name__)

model = joblib.load('model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        review = request.form['review']
        preprocessed_review = preprocess(review)
        # print("preprocessed review:",preprocessed_review)
        vectorized_review = vectorizer.transform([preprocessed_review])
        prediction = model.predict(vectorized_review)
        probability = model.predict_proba(vectorized_review)
        rating = round(probability[0][1]*10)
        color_class = 'text-green-500' if prediction[0] == 'positive' else 'text-red-500'
        # print(probability[0])
        return render_template('results.html',prediction=prediction[0].capitalize(),color_class=color_class,prob_pos=round(probability[0][1],3),prob_neg=round(probability[0][0],3),rating=rating)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
