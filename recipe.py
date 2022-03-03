from instaloader import Instaloader, Profile
import random
import requests
import json
import config
from dotenv import load_dotenv


lista=['keto.meals.life','cleaneatfeed','real.foodie','lastingredient','healthy_recipes_from_annette','the_healthy_work_shop','lafit_ruffina_incucina',
'bringingithome_'
       ]

index=[]
n=0
while n < len(lista):
    index.append(n)
    n=n+1

m=random.choice(index)
print(m)
PROFILE = lista[m]
print(PROFILE)

MAX_DAYS = 10
L = Instaloader()
img=[]
texto=[]
profile = Profile.from_username(L.context, PROFILE)

# for post in profile.get_posts():
#     print(post.url)
#     print(post.caption)

for post in profile.get_posts():
    n=n+1
    change = post.url
    caps= post.caption
    texto.append(caps)
    img.append(change)
    if (n > MAX_DAYS):
        break

page_id_1 = 100133808925157
facebook_access_token_1 = config.token


msg = texto[m]
image_location = img[m]
image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)

print (msg)
print (image_location)
img_payload = {
        'message': msg,
        'url': image_location,
        'access_token': facebook_access_token_1
}
    # Send the POST request
r = requests.post(image_url, data=img_payload)
print(r.text)

def postInstagramQuote(token=token):
#Post the Image
    id=17841448178862039
    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(id)
    payload = {
    'image_url': image_location,
    'caption': msg,
    'access_token': token
    }
    r = requests.post(post_url, data=payload)
    print(r.text)
    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        second_url = 'https://graph.facebook.com/v10.0/{}/media_publish'.format(id)
        second_payload = {
        'creation_id': creation_id,
        'access_token': token
        }
        r = requests.post(second_url, data=second_payload)
        print('--------Just posted to instagram--------')
        print(r.text)
    else:
        print('HOUSTON we have a problem')
postInstagramQuote()
