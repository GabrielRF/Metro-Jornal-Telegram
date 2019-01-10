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
hoje = now.strftime('%d/%m/%Y')
city = city

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

if __name__ == '__main__':
    sent = get_ed()
    attemp = 4
    while sent == 0 and attemp < 5:
        time.sleep(900)
        attemp = attemp + 1
        sent = get_ed()

