from clarifai.rest import ClarifaiApp
from clarifai_auth import *

app = ClarifaiApp(CLARIFAI_APP_ID,CLARIFAI_APP_SECRET)

#models
nsfw_model = app.models.get('nsfw-v1.0')
general_model = app.models.get('general-v1.3')
pets_model = app.models.get('pets')
friend_identifier = app.models.get('friend_indentifier')

models = {'nsfw': nsfw_model, 'general' : general_model, 'pets' : pets_model, 'friend_identifier' : friend_identifier}

#Choose model
print('Available models are: ')
for key in models.keys():
    print(key)

model = models[input('\nEnter your desired model ')]

method = input('Would you like to use a url or a filepath? ')

if method == 'url':
    result = model.predict_by_url(url=input('Enter the url of an image you would like to analyze '))
elif method == 'filepath':
    result = model.predict_by_filename(filename=input('Enter the path to a file that you would like to use '))
"""
for key in result.keys():
    print("Name:" + key + " Type: " + str(type(result[key])))
"""

outputs = result['outputs'][0]
data = outputs['data']
concepts = data['concepts']

"""
#find specific concept value
desired_concept = 'cute cat'
concept_result = None

for c in concepts:
    if c['name'] == desired_concept:
        concept_result = c

print(concept_result['name'] + ': ' + str(concept_result['value']))
"""

#list all concepts and values
for c in concepts:
    print(c['name'] + ': ' + str(c['value']))
