import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyze } }

    try:
        res =  requests.post(url, headers=headers, json=json)

        if res.status_code == 200:
            emotion_data = res.json()
            emotions = emotion_data.get('emotionPredictions',{})[0].get("emotion")
            # print(emotion_data)
            required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
            extracted_emotions = {emotion: emotions.get(emotion) for emotion in required_emotions}
            
            dominant_emotion = max( extracted_emotions, key=extracted_emotions.get)
            print("dom:", dominant_emotion)
            extracted_emotions['dominant_emotion'] = extracted_emotions[dominant_emotion]
            return dominant_emotion
        else:
            return f"Error: {res.status_code}, {res.text}"
    except Exception as e:
        return f"An Error occured {str(e)}"
