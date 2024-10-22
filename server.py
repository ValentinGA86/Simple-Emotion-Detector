from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the emotion detector
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Extract the input text from the form
    input_text = request.form.get('text')
    
    # Run the emotion detection on the input text
    result = emotion_detector(input_text)
    
    # Handle case where dominant emotion is None (error or blank input)
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again."}), 400
    
    # Format the response
    response = (f"For the given statement, the system response is 'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
                f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.")
    
    # Return the result as a JSON response
    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

