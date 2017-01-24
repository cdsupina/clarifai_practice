from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai_auth import *

#app = ClarifaiApp('{CLARIFAI_APP_ID}','{CLARIFAI_APP_SECRET}')
app = ClarifaiApp(CLARIFAI_APP_ID,CLARIFAI_APP_SECRET)

model = app.models.get('general-v1.3')

print(model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg'))
