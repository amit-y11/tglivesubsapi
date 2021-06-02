import requests
from bs4 import BeautifulSoup as bs

def scrape(channel):
    try:
        page=requests.get("https://telegram.dog/"+channel)
        soup=bs(page.text,'html.parser')
        subs=soup.find("div",{"class":'tgme_page_extra'}).text.replace(" ","").split("subscribers")[0]
        channel_name=soup.find("div",{"class":'tgme_page_title'}).text.replace("\n","")
        description=soup.find("div",{"class":'tgme_page_description'}).text
        img=soup.find("img",{"class":'tgme_page_photo_image'})['src']
        data = {}
        data['subs']=subs
        data['channel_name']=channel_name
        data['description']=description
        data['image']=img
        return data
    except Exception as e:
        return {"Error":e}


