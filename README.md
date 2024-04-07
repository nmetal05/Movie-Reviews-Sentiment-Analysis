# Movie Review Sentiment Analysis

This project is a Flask web application that takes a movie review as input and returns the predicted sentiment and probability of being positive or negative.

## Deployed Version

You can view the deployed version of this application at :

[Movie Review Sentiment Analysis](https://movie-reviews-sentiment-analysis.onrender.com)

## Requirements

* Python 3.6 or later
* Flask
* gunicorn
* joblib
* scikit-learn
* nltk
* bs4
  
## Installation

1. Clone the repository :
```bash
git clone https://github.com/nmetal05/movie-reviews-sentiment-analysis
```
2. Navigate to the project directory  :
```bash
cd movie-review-sentiment-analysis
```
3. Create a virtual environment and activate it using your preffered shell :
```bash
python -m venv venv
source venv/bin/activate
```
4. Install the required dependencies :
```bash
pip install -r requirements.txt
```
5. Start the application locally using Gunicorn(or Flask) :
```bash
gunicorn app:app
```
```bash
flask run
```
6. The application will be available at :
* If you used Gunicorn: <http://127.0.0.1:8000/>
* If you used flask run: <http://127.0.0.1:5000/>

## Usage

To use the application, simply enter a movie review in the textarea and click the "Analyze Review" button. The predicted sentiment and probability of the review being positive or negative will be displayed along with the rating.

