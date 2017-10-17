from datetime import datetime
import requests

now = datetime.now()
today = now.strftime('%Y%m%d')
hoje = now.strftime('%d/%m/%Y')
city = 'Brasilia'

cover = 'https://www2.metrojornal.com.br/pdf/assets/capas/{}_{}_Capa.jpg'.format(today, city)
pdf = 'https://www2.metrojornal.com.br/pdf/assets/pdfs/{}_{}.pdf'.format(today, city)

response = requests.get(cover)
print(response.status_code)

if 200 != response.status_code:
    print('fail')
else:
    print(cover)
    print(pdf)

    message = ('Metro Jornal<a href="{}">.</a>'.format(cover) +
        '\n<b>{}</b> {}'.format(city, hoje) +
        '\n<a href="{}">PDF</a>'.format(pdf))

    print(message)
