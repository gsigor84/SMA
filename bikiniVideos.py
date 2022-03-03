from instaloader import Instaloader, Profile
import random
import requests
import config
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




lista=['janetlayug','jenniferdorie_ifbbpro','etila','angelicaht','lauraliechap','isapecini','jazzyfresh.ifbbpro','Breena Martinez','sommerray','kayla_itsines'
       ,'zuzkalight','ashleykfit','paigehathaway','rominabass','bellsbodyfit',
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

MAX_DAYS = 20
L = Instaloader()
img=[]
texto=[]
profile = Profile.from_username(L.context, PROFILE)

# for post in profile.get_posts():
#     print(post.url)
#     print(post.caption)

for post in profile.get_posts():
    n=n+1
    change = post.video_url
    caps= post.caption
    if post.is_video:
        # texto.append(caps)
        img.append(change)
    if (n > MAX_DAYS):
        break

page_id_1 = 100133808925157
facebook_access_token_1 = config.token


msg = 'InstaVideos'+'@'+PROFILE
image_location = img[0]
image_url = 'https://graph-video.facebook.com/{}/videos'.format(page_id_1)
desc ='🔥🏋️‍♂️🏆   InstaVideos+@'+PROFILE+' 🏋️‍♂️🔥\n\n#workout #coreworkout #backworkout #hiitworkout #homeworkouts #morningworkout #iworkout #girlswhoworkout #cardioworkout #legworkout #workoutoftheday'
print (msg)
print (image_location)
img_payload = {

        'title': msg,
'file_url': image_location,
        'access_token': facebook_access_token_1,
'description': desc
}
    # Send the POST request
r = requests.post(image_url ,data=img_payload, verify=False)
print(r.text)