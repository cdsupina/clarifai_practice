from clarifai_auth import *
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(CLARIFAI_APP_ID,CLARIFAI_APP_SECRET)

for i in range(0,10):
    app.inputs.create_image_from_filename(filename='frames/26-01-2017/' + str(i) + '.png', concepts=['carlo'])



model = app.models.create(model_id="friend_indentifier", concepts=['carlo'])

model = model.train()

