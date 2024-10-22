from transformers import pipeline

# Load Hugging Face model
emotion_model = pipeline('text-classification', model="cardiffnlp/twitter-roberta-base-emotion")

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        # Handle blank input
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    # Use model to analyze emotions
    result = emotion_model(text_to_analyze)[0]
    
    emotions = {
        'anger': result['score'] if result['label'] == 'anger' else 0,
        'disgust': result['score'] if result['label'] == 'disgust' else 0,
        'fear': result['score'] if result['label'] == 'fear' else 0,
        'joy': result['score'] if result['label'] == 'joy' else 0,
        'sadness': result['score'] if result['label'] == 'sadness' else 0,
        'dominant_emotion': result['label']
    }
    return emotions
