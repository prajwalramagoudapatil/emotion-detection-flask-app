import unittest
import sys
import os

# Add the parent directory to the Python path so Python can find the emotiondetection package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from emotiondetection.emotion_detection import emotion_detector

class TestEmotions(unittest.TestCase):
    def test_emotion_detector(self):
       test_cases = [
        {'text': 'I am glad this happened', 'emotion':	'joy'},
        {'text': 'I am really mad about this', 'emotion': 'anger'},
        {'text': 'I feel disgusted just hearing about this', 'emotion': 'disgust'},
        {'text': 'I am so sad about this', 'emotion':	'sadness'},
        {'text': 'I am really afraid that this will happen', 'emotion':	'fear'},
       ]
       test_res = [ emotion_detector( test.get('text') ) for test in test_cases ]
       expected_res = [test.get('emotion') for test in test_cases]

       self.assertEqual(test_res, expected_res)

if __name__ == '__main__':
    unittest.main()