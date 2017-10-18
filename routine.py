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
now = datetime.now()
today = now.strftime('%Y%m%d')
hoje = now.strftime('%d/%m/%Y')

cover = 'https://www2.metrojornal.com.br/pdf/assets/capas/{}_{}_Capa.jpg'.format(today, arg)
pdf = 'https://www2.metrojornal.com.br/pdf/assets/pdfs/{}_{}.pdf'.format(today, arg)
bot = telebot.TeleBot(token)

def get_ed():
    response = requests.get(cover)
    if 200 != response.status_code:
        print('fail')
        return 0
    else:
        message = ('\U0001F4F0 <b>{}</b><a href="{}">.</a> #{}'.format(city, cover, city.replace(' ','')) +
            '\n{}'.format(hoje) +
            '\n<a href="{}">Arquivo PDF</a>'.format(pdf))
        bot.send_message('9083329', message, parse_mode='HTML')
        return 1

if __name__ == '__main__':
    sent = get_ed()
    while sent == 0:
        time.sleep(900)
        sent = get_ed()
        


