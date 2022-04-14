import sys
import webbrowser


f = str(sys.argv[1])
print("Você buscou pela palavra: {} ".format(f))

google = "https://www.google.com/search?tbm=isch&q={}".format(f)
taoeba = "https://tatoeba.org/en/sentences/search?from=eng&has_audio=&native=&orphans=no&query={}&sort=relevance&sort_reverse=&tags=&to=por&trans_filter=limit&trans_has_audio=&trans_link=&trans_orphan=&trans_to=&trans_unapproved=&trans_user=&unapproved=no&user=".format(f)
wordreference = "https://www.wordreference.com/enpt/{}".format(f)
forvo = "https://forvo.com/word/{}/#en_usa".format(f)
cambridge = "https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}".format(f)

webbrowser.open(taoeba,new=2)
webbrowser.open(wordreference,new=2)
webbrowser.open(cambridge,new=2)
webbrowser.open(google,new=2)
webbrowser.open(forvo,new=2)