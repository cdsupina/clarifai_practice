from clarifai_auth import *
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(CLARIFAI_APP_ID,CLARIFAI_APP_SECRET)

app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog2.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])

app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat1.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat2.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])

model = app.models.create(model_id="pets", concepts=["cute cat", "cute dog"])

model = model.train()

print (model.predict_by_url(url="https://samples.clarifai.com/dog3.jpeg"))
print (model.predict_by_url(url="https://samples.clarifai.com/cat3.jpeg"))
