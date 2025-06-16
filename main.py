from com.atividade1.lemmatization.NltkWordNet import NltkWordNet

if __name__ == "__main__":
    nwn = NltkWordNet()
    #Exemplo1;
    print(nwn.verbify("writer"))
    #Exemplo2;
    print(nwn.nounify("written"))
