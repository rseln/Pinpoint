import os, io
from google.cloud import vision

image_file = "picture.jpg"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'object-recognition-key.json'

client = vision.ImageAnnotatorClient()

path = "picture.jpg"

with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content) # pylint: disable=no-member

response = client.object_localization(image=image) # pylint: disable=no-member

print('Labels (and confidence score):')
print('=' * 79)

for label in response.label_annotations:
    print(f'{label.description} ({label.score*100.:.2f}%)')