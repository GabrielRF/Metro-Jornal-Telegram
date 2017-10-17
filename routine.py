from datetime import datetime
import configparser
import requests
import sys
import telebot

arg = sys.argv[1]

config = configparser.ConfigParser()
config.sections()
config.read('bot.conf')

token = config[arg]['TOKEN']
city = config[arg]['CITY']

now = datetime.now()
today = now.strftime('%Y%m%d')
hoje = now.strftime('%d/%m/%Y')

cover = 'https://www2.metrojornal.com.br/pdf/assets/capas/{}_{}_Capa.jpg'.format(today, arg)
pdf = 'https://www2.metrojornal.com.br/pdf/assets/pdfs/{}_{}.pdf'.format(today, arg)

response = requests.get(cover)
bot = telebot.TeleBot(token)

if 200 != response.status_code:
    print('fail')
else:
    message = ('<b>{}</b><a href="{}">.</a>'.format(city, cover) +
        '\n{}'.format(hoje) +
        '\n<a href="{}">Arquivo PDF</a>'.format(pdf))
    bot.send_message('@MetroJornal', message, parse_mode='HTML')
