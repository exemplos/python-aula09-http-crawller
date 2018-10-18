
from urllib.request import Request, urlopen  # Python 3

q = Request('http://www.rmtcgoiania.com.br/index.php?option=com_rmtclinhas&view=pedhorarios&format=raw&ponto=1481')
q.add_header('Cookie', '__cfduid=d2a2c2fa5590a82b0f62fa44e31a94b491538179618; 4029dc09fae2b24f3d2ae3d2b169a292=679942c987cf74f4c0b70f51ed879bea; __utma=126153870.207967529.1538179620.1538179620.1538179620.1; __utmc=126153870; __utmz=126153870.1538179620.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=126153870.9.10.1538179620')
q.add_header('Host', 'www.rmtcgoiania.com.br')
q.add_header('Referer', 'http://www.rmtcgoiania.com.br/index.php/pontos-embarque-desembarque?query=1481&uid=5baec3a1dc04e')
q.add_header('Upgrade-Insecure-Requests', '1')
q.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
a = str(urlopen(q).read())

print(a.find('<table'))

table = a[a.find('<table') : a.find('</table')]

print(table)