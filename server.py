from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

"""
This package was created  as part of an assessment for the IBM course web app using Flask
created by Chris Rees 21/09/23
"""

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)

    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    else:
        return "For the given statement, the system response is {}.".format(dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
