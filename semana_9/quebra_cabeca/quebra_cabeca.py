import urllib.request
import urllib.error
from unicodedata import normalize


def separar_data(dma):
    a = dma % 10000
    dma //= 10000
    m = dma % 100
    dma //= 100
    d = dma
    return d, m, a


def signo(dia, mes):
    if not (1 <= mes <= 12 and 1 <= dia <= 31):
        return None

    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'


def remover_acentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


def horoscopo(signo_desejado):
    signo_formatado = remover_acentos(signo_desejado).lower()
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    try:
        resposta = urllib.request.urlopen(requisicao, timeout=10)
        pagina = resposta.read().decode('utf-8')
    except urllib.error.URLError as erro:
        return f"Erro ao acessar o site: {erro.reason}"

    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    pos_marcador = pagina.find(marcador_inicio)
    
    # Verifica se o marcador realmente existe no HTML atual do site
    if pos_marcador == -1:
        return f"{signo_desejado}: Não foi possível extrair o texto (o layout do site mudou)."

    inicio = pos_marcador + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ': ' + pagina[inicio:final].strip()


def main():
    try:
        nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))
    except ValueError:
        print("Erro: Digite apenas números no formato DDMMAAAA.")
        return

    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)

    if meu_signo is None:
        print("Erro: Data inválida.")
        return

    horoscopo_de_hoje = horoscopo(meu_signo)
    print(horoscopo_de_hoje)


if __name__ == '__main__':
    main()