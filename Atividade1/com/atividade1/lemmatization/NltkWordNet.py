from nltk.corpus import wordnet as wn

class NltkWordNet:
    def __init__(self):
        pass

    def __lemmatize(self, word, pos_word, to_pos):
        """ 
            Retorna a lista de palavras da classe gramatical (adv, adj, verb, noun) passada em pos_word e que possuam o mesmo conceito
            (sejam sinonimos) da palavra (word) informada;
        """
        pos_list = wn.synsets(word, pos_word)

        #Caso nao seja encontrada nenhuma palavra, return [];
        if not pos_list:
           return []

        """ 
            Neste ponto, notamos uma redundancia no codigo recomendado pelo stack overflow, pois
            o autor do codigo faz uma filtragem de acordo com a classe gramatical informada, sendo
            que essa filtragem ja e feita pela funcao synsets quando este e passado no segundo parametro
            da funcao

            word_lemmas = [s.lemmas() for s in pos_list if s.name().split('.')[1] == pos_word]
        """
        
        #Cria uma lista com os lemas das palavras listadas pela funcao synsets (uma palavra pode ter um ou mais lemmas);
        word_lemmas = [s.lemmas() for s in pos_list]
        
        #Caso nao seja encontrado nenhum lemma associado a palavra, return [];
        if not word_lemmas:
           return []

        #Lista as diferentes flexibilizacoes dos lemmas listados em word_lemmas;
        derivationally_related_forms = [(l, l.derivationally_related_forms()) for l in word_lemmas[0]]

        #Das possiveis flexibilizacoes, filtra somente os que sao da classe gramatical informada em to_pos (adv, adj, noun ou verb);
        filtered_noun_lemmas = [drf[1] for drf in derivationally_related_forms
                                for l in drf[1] if l.synset().name().split('.')[1] == to_pos][0]
        
        #Retorna a lista de nomes vinculados a filtered_noun_lemmas;
        words = [l.name() for l in filtered_noun_lemmas]
        words_len = len(words)

        #Lista (word, frequency);
        words_probability = [(w, float(words.count(w))/words_len) for w in set(words)]

        #Ordena a lista em funcao da probabilidade de ocorrencia da palavra w em words;
        return sorted(words_probability, key=lambda w:-w[1])

    #Verb --> Noun
    def nounify(self, word):
        return self.__lemmatize(word, wn.VERB, wn.NOUN)

    #Noun --> Verb
    def verbify(self, word):
        return self.__lemmatize(word, wn.NOUN, wn.VERB)
