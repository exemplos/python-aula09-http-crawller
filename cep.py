from urllib.parse import urlencode
from urllib.request import Request, urlopen

parametros = {"relaxation":"74265020", "tipoCEP": "ALL", "semelhante": "N"}

url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm"

req =  Request(url, urlencode(parametros).encode())
result = urlopen(req).read()
result = str(result)

find = "CEP:</th>"
posicao = int(result.index(find) + len(find))
texto = result[posicao : posicao + 200]

print(texto)

