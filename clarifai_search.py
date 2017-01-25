from clarifai_auth import *
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(CLARIFAI_APP_ID,CLARIFAI_APP_SECRET)

# before search, first need to upload a few images
app.inputs.create_image_from_url("https://samples.clarifai.com/puppy.jpeg",allow_duplicate=True)

# search by predicted concept
print(app.inputs.search_by_predicted_concepts(concept='dog'))
