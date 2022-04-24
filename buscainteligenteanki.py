import sys
import webbrowser

f = input('$ ')
print("Você buscou pela palavra: {} ".format(f))

googleimage = "https://www.google.com/search?tbm=isch&q={}".format(f)
taoeba = "https://tatoeba.org/en/sentences/search?from=eng&has_audio=&native=&orphans=no&query={}&sort=relevance&sort_reverse=&tags=&to=por&trans_filter=limit&trans_has_audio=&trans_link=&trans_orphan=&trans_to=&trans_unapproved=&trans_user=&unapproved=no&user=".format(f)
wordreference = "https://www.wordreference.com/enpt/{}".format(f)
linguee = "https://www.linguee.com.br/portugues-ingles/search?source=ingles&query={}".format(f)
forvo = "https://forvo.com/word/{}/#en_usa".format(f)
cambridge = "https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}".format(f)
michaelis = "https://michaelis.uol.com.br/moderno-ingles/busca/ingles-portugues-moderno/{}".format(f)
reverso = "https://context.reverso.net/traducao/ingles-portugues/{}".format(f)
translate = "https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&text={}".format(f)


webbrowser.open(taoeba,new=2)
webbrowser.open(wordreference,new=2)
webbrowser.open(cambridge,new=2)
webbrowser.open(linguee,new=2)
webbrowser.open(googleimage,new=2)
webbrowser.open(forvo,new=2)
webbrowser.open(michaelis,new=2)
webbrowser.open(reverso,new=2)
webbrowser.open(translate,new=2)
