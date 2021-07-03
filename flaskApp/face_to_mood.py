#receives face, returns mood


from fer import FER
from cv2 import imread
from pprint import pprint,pformat

weights = {
    "disgust" : -2,
    "angry" : -2,
    "fear" : -1,
    "sad" : -1,
    "neutral" : 1,
    "surprise" : 0,
    "happy" : 3
    }

# takes an image file and returns the emotions found in it weighted
# to suit music recommendation purposes
def give_result(image : str):
    result = [] 

    img = imread(image)
    if img is None:
       return f"CANNOT_READ_IMAGE {image}"
    detector = FER()
    
    detection = detector.detect_emotions(img)[0]['emotions']

    suggest = ['Happy']
    expectation = sum([weights[emo]*detection[emo] for emo in detection])
    if expectation < 0.2:
        suggest = ['Sad', 'Calm']
    elif expectation < 1.2:
        suggest = ['Calm', 'Happy', 'Energetic']
    else:
        suggest = ['Happy', 'Energetic']
    return suggest
