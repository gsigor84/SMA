from instaloader import Instaloader, Profile
import random
import requests
import json
import config
import HashTagMotivation


# nutrition

lista=['trainitright','armoy_fitlab','dstrong.fitnessmotivation','arnold_schwarzenegger_photos']
index=[]
n=0
while n < len(lista):
    index.append(n)
    n=n+1


m=random.choice(index)
print(m)
PROFILE = lista[m]
print(PROFILE)
L = Instaloader()

MAX_DAYS = 10

img=[]

profile = Profile.from_username(L.context, PROFILE)
n=0

for post in profile.get_posts():
    n=n+1
    change = post.url
    img.append(change)
    if (n > MAX_DAYS):
        break



print(random.choice(img))

def postInstagramQuote(token=config.token):
#Post the Image
    id=17841448178862039
    token= token
    image_location_1 = random.choice(img)
    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(id)
    payload = {
    'image_url': image_location_1,
    'caption': 'follow @cubanfit_91'+HashTagMotivation.hashtag,
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

