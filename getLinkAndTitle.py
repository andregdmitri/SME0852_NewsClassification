import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def getTitleAndLink(news = 'g1'):
  if (news == 'g1'):
    home_link = "https://g1.globo.com"
    res = requests.get(home_link)
    soup = BeautifulSoup(res.content, 'html.parser')
    link_and_title = soup.find_all('div',{'class':'_evt'})
  elif(news == 'r7'):
    home_link = "https://www.r7.com"
    res = requests.get(home_link)
    soup = BeautifulSoup(res.content, 'html.parser')
    link_and_title = soup.find_all('div',{'class':'widget-8x1-e__title'})
  link_and_title_list = []
  for i in range(len(link_and_title)):
    title = link_and_title[i].text
    link = link_and_title[i].a['href']
    link_and_title_list.append([title, link])
  df = pd.DataFrame(link_and_title_list, columns = ['title', 'link'])
  #df.to_csv('linkNtitle.csv')
  return df

def getBody():
  df = getTitleAndLink()
  body_list = []
  for link in df['link']:
    info_list = []
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')
    info = soup.find_all('p',{'class':"content-text__container"})
    for i in info:
      info_list.append(i.get_text())
    body_list.append(info_list)
  #df2 = pd.DataFrame(info_list, columns = ['body'])
  df['body'] = body_list
  return df