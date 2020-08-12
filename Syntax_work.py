
import spacy
import sys
from collections import Counter
nlp_fr = spacy.load('fr')

class Textfile:

    def __init__(self, name, encoding="utf-8"):

        self._name = name
        self._encoding = encoding
        self._content = ""

    def read(self):
        try:
            f = open(self._name, encoding=self._encoding, mode='r')
            self._content = f.read()

            f.close()
        except OSError as err:
            print("OS error: {0}".format(err))

    def calcul(self, outputfile):
        try:
            f = open(outputfile, encoding=self._encoding, mode='w')
            verbs={}
            doc=nlp_fr(self._content)

            counts=Counter()
            #calcul d'occurences de chaque verbe
            for sent in doc.sents:
                for tok in sent:
                    # skip spaces
                    if tok.pos_ == 'SPACE': continue
                    if tok.pos_ == "VERB":
                        counts[tok.lemma_]+=1
            #créer une liste ordonnée de tous les verbes (ordonnée en fonction du nombre d'occurences)
            verbes = sorted(counts, key=counts.get, reverse=True)
            #créer un dictionnaire qui a comme clé le verbe et comme valeurs les pourcentages des compléments

            # chercher les compléments pour chaque lemme verbal
            #dictionnaire avec tous les compléments
            
            for verb in verbes:
                complements={'obj':0,'obl':0,'iobj':0,'ccomp':0,'xcomp':0}
                for sent in doc.sents:
                    for tok in sent:
                        # skip spaces
                        if tok.pos_ == 'SPACE': continue
                        #si le mot est dépendant du verbe
                        if tok.head.text == verb:
                            for key in complements.keys():
                                if tok.dep_==key:
                                    complements[key]+=1
                for key in complements.keys():
                    # on calcule les pourcentages
                    complements[key] = int(complements[key]*100/counts[verb])
                # pour chaque verbe on écrit dans le fichier le nombre d'occurences
                f.write(str(counts[verb]))
                f.write(" ")
                # le lemme verbal
                f.write(verb)
                f.write(" ")
                #et les pourcentages
                f.write(str(complements))
                f.write("\n")

            f.close()
        except OSError as err:
            print("OS error: {0}".format(err))


def main():
    #condition d'existence du paramètre
    if sys.argv is None or len(sys.argv) <2:
        print("you need to insert the name of the file")
        exit()

    filename = sys.argv[1] #le programme prend comme parametre le nom du fichier
    tf=Textfile(filename) #on instantie la classe Textfile
    tf.read() #on appelle la fonction read() pour lire le fichier
    tf.calcul("verbes.txt") #appel de la fonction calcul





if __name__ == "__main__":
    main()
