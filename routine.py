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

url = 'https://www.readmetro.com/pt/brazil/{}/{}/1/'.format(city.lower(),todayclean)
cover = 'https://www2.metrojornal.com.br/pdf/assets/capas/{}_{}_Capa.jpg'.format(today, arg)
pdf = 'https://rm.metrolatam.com/pdf/{}{}.pdf'.format(today, arg.lower())
bot = telebot.TeleBot(token)

def get_ed():
    message = ('<a href="{}">\U0001F4F0</a> #{}'.format(cover, city.replace(' ','')) +
        '\n{}'.format(hoje) +
        '\n<a href="{}">Arquivo PDF</a>'.format(pdf))
    for i in dest.split(','):
        bot.send_message(i, message, parse_mode='HTML')
    return 1

def get_img(url):
    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')
    img = html.find('meta', {'property': 'og:image'})
    if not img:
        img = html.find('meta', {'name': 'og:image'})
    try:
        img = img['content']
        preview = False
        if 'http:' not in img and 'https:' not in img:
            img = 'http:' + img
    except TypeError:
        img = ''
        preview = True
    return preview, img


if __name__ == '__main__':
    preview, cover = get_img(url)
    sent = get_ed()
    attemp = 4
    while sent == 0 and attemp < 5:
        time.sleep(900)
        attemp = attemp + 1
        sent = get_ed()

