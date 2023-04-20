import argparse
import click
import eng_to_ipa as ipa
import webbrowser
from termcolor import colored
import os
import shlex

parser = argparse.ArgumentParser(description='Escolha uma opção')
parser.add_argument('--opcao', type=int, help='Digite o número da opção que deseja')

options = {
    1: 'Mineração de palavras',
    2: 'Trancrição IPA',
    3: 'Sair'
}


if __name__ == '__main__':
    args = parser.parse_args()
    opcao = args.opcao

    if opcao in options:
        print('Você escolheu a opção', opcao, ':', options[opcao])
    else:
        print('Opção inválida')


# Função que executa a opção 1
def minerar_palavras():
    while True:
        # Insira aqui o código para minerar palavra
        f = input(colored('$ ', 'green'))
        resp = ipa.convert(f)
        print(colored("Em IPA a pronuncia correta seria: ", 'blue'), resp)
        print(colored("Você buscou pela palavra: {} ".format(f), 'magenta'))
    
        # Define as URLs dos sites de referência para a palavra pesquisada
        googleimage = "https://www.google.com/search?tbm=isch&q={}".format(f)
        taoeba = "https://tatoeba.org/pt-br/sentences/search?from=eng&query={}&to=por".format(f)
        wordreference = "https://www.wordreference.com/definition/{}".format(f)
        linguee = "https://www.linguee.com.br/portugues-ingles/search?source=ingles&query={}".format(f)
        forvo = "https://forvo.com/word/{}/#en_usa".format(f)
        cambridge = "https://dictionary.cambridge.org/dictionary/english-portuguese/{}".format(f)
        michaelis = "https://michaelis.uol.com.br/moderno-ingles/busca/ingles-portugues-moderno/{}".format(f)
        reverso = "https://www.reverso.net/tradu%C3%A7%C3%A3o-texto#sl=eng&tl=por&text={}".format(f)
        collins = "https://www.collinsdictionary.com/pt/dictionary/english/{}".format(f)
        translateuk = "https://translate.google.co.uk/?sl=en&tl=pt&text={}".format(f)
        oxford = "https://www.oxfordlearnersdictionaries.com/us/definition/english/{}".format(f)
        deepl = "https://www.deepl.com/translator#en/pt/{}".format(f)
        youglish = "https://pt.youglish.com/pronounce/{}/english/uk".format(f)
        bab = "https://en.bab.la/dictionary/english-portuguese/{}".format(f)
        pons = "https://en.pons.com/translate/english-portuguese/{}".format(f)
        glosb = "https://glosbe.com/en/pt/{}".format(f)
        rev = "https://conjugator.reverso.net/conjugation-english-verb-{}.html".format(f)


#        webbrowser.open(forvo,new=2)
#        webbrowser.open(linguee,new=2)
#        webbrowser.open(michaelis,new=2)
        #webbrowser.open(oxford,new=2)
#        webbrowser.open(reverso,new=2)
#        webbrowser.open(googleimage,new=2)
        webbrowser.open(taoeba,new=2)
#        webbrowser.open(translateuk,new=2)
#        webbrowser.open(deepl,new=2)
        webbrowser.open(cambridge,new=2)
#        webbrowser.open(collins,new=2)
#        webbrowser.open(youglish, new=2)
        webbrowser.open(bab,new=2)
        #webbrowser.open(pons,new=2)
        webbrowser.open(glosb,new=2)
        webbrowser.open(rev,new=2)

        # Pergunta se deseja continuar
        #resposta = input("deseja continuar minerando? (y/n)")
        #if resposta.lower() == "n":
        #   return  # Retorna quando o loop é interrompido

# Função que executa a opção 2x
def ver_ipa():
    while True:
        # Insira aqui o código para ver o IPA
        f = shlex.quote(input(colored('$ ', 'green')))
        f = f.strip("'")  # Remove as aspas da entrada do usuário
        output = os.popen("curl -X POST 'https://www.phonetizer.com/phonetizer/default/call/jsonrpc?nocache=1681283729374' -H 'Content-Type: application/json' --data-raw '{\"service\":\"\",\"method\":\"transcribe\",\"id\":3,\"params\":[\"" + f + "\",\"British\"]}' --silent | json_pp | cut -d \"/\" -f 7 | cut -d \",\" -f 2 | cut -d '\"' -f 1 ").read()
        print("A transcrição fonética é:", colored(output.strip().replace('\n', ' ').replace('{','').replace('}',''), 'cyan'))

        # Pergunta se deseja continuar
        #resposta = input("Deseja continuar visualizando o IPA? (y/n): ")
        #if resposta.lower() == "n":
        #    return  # Retorna quando o loop é interrompido





@click.command()
@click.option('--opcao', type=int, help='Digite o número da opção que deseja')
def menu(opcao):
    while opcao != 3:
        if opcao == 1:
            minerar_palavras()
        elif opcao == 2:
            ver_ipa()
        else:
            print("Opção inválida. Digite um número de 1 a 3.")

        # Mostra as opções novamente
        print(" ")
        print("O que você deseja?")
        print("1) Mineração de palavras")
        print("2) Transcrição IPA")
        print("3) Sair")
        print(" ")
        print(" ")

        
        # Pede a opção ao usuário
        opcao = int(input("Digite o número da opção: "))


if __name__ == "__main__":
    menu()
