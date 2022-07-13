import requests
import json
from cred import access_token,page_id

image_location='https://wallpaperaccess.com/full/7476.jpg'
caption='Posted by python Script'

get_ig_id_url=f'https://graph.facebook.com/v14.0/{page_id}'
payload1={
    "fields":"instagram_business_account",
    "access_token":access_token
}
res1=requests.get(get_ig_id_url,payload1)
# print(res1.text)
ig_id=(json.loads( res1.text))['instagram_business_account']['id']
# print(ig_id)

get_creation_id_url=f'https://graph.facebook.com/{ig_id}/media'
payload2={
    'image_url':image_location,
    'caption':caption,
    'access_token':access_token
}
res2=requests.post(get_creation_id_url,payload2)
creation_id=(json.loads( res2.text))['id']
# print(creation_id)

publish_media=f'https://graph.facebook.com/{ig_id}/media_publish'
payload3={
    'creation_id':creation_id,
    'access_token':access_token
}

res3=requests.post(publish_media,payload3)
final=json.loads(res3.text)
if 'id' in final:
    print(final['id'])
    print('posted successfully')
else:
    print('Error while posting')




# instagram page is needed, we can get it by facebook settings
# access_token is needed by developer.facebook.com of this page