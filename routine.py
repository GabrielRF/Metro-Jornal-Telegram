from bs4 import BeautifulSoup
from datetime import datetime
import configparser
import requests
import sys
import telebot
import time

arg = sys.argv[1]

config = configparser.ConfigParser()
config.sections()
config.read('bot.conf')

token = config[arg]['TOKEN']
city = config[arg]['CITY']
dest = config[arg]['DEST']
now = datetime.now()
today = now.strftime('%Y/%m/%d/%Y%m%d_')
todayclean = now.strftime('%Y%m%d')
hoje = now.strftime('%d/%m/%Y')
city = city

url = 'https://www.readmetro.com/pt/brazil/{}/{}/1/'.format(arg.lower(),todayclean)
cover = 'https://www2.metrojornal.com.br/pdf/assets/capas/{}_{}_Capa.jpg'.format(today, arg)
pdf = 'https://www.readmetro.com/pt/brazil/{}/{}/1/'.format(arg.lower(), todayclean)
bot = telebot.TeleBot(token)

def get_ed(cover, pdf):
    message = ('<a href="{}">\U0001F4F0</a> #{}'.format(cover, city.replace(' ','')) +
        '\n{}'.format(hoje) +
        '\n<a href="{}">Clique aqui para ler</a>'.format(pdf))
    print(message)
    for i in dest.split(','):
        bot.send_message(i, message, parse_mode='HTML')

def get_img(url):
    print(url)
    response = requests.get(url)
    if '404!' in response.text:
        return False, None
    html = BeautifulSoup(response.content, 'html.parser')
    img = html.find('meta', {'property': 'og:image'})
    if not img:
        img = html.find('meta', {'name': 'og:image'})
    try:
        img = img['content']
        if 'http:' not in img and 'https:' not in img:
            img = 'http:' + img
    except TypeError:
        img = ''
        return False, None
    print(img)
    return True, img

if __name__ == '__main__':
    preview, cover = get_img(url)
    print(preview)
    if preview == True:
        get_ed(cover, pdf)

