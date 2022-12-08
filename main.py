import requests

from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    
    requisicao_dis = requisicao.json()

    cotacao_dolar = requisicao_dis['USDBRL']['bid']
    cotacao_euro = requisicao_dis['EURBRL']['bid']
    cotacao_btc = requisicao_dis["BTCBRL"]['bid']

    texto = f'''

    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}'''

    texto_cotacoes["text"] = texto

janela = Tk()

janela.title("cotação de moedas")

janela.geometry("350x225")

texto_orientacao = Label(janela, text="clique no botão para exibir as cotações das moedas")

texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

texto_orientacao2 = Label(janela, text="clique aqui agora")

texto_orientacao2.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="buscar cotações", command=pegar_cotacoes)

botao.grid(column=0, row=2, padx=10, pady=10)

texto_cotacoes = Label(janela, text="")

texto_cotacoes.grid(column=0, row=3)


janela.mainloop()