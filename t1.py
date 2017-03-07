for i in range(5): #iteracja
    print(i)

a = [i for i in range(6)] #budowanie listy
print(a)

a = [(i,i*2) for i in range(6)] #budowanie listy par
print(a)

n = [3]
a = [(i,i*2) for i in range(6) if i not in n] #lista par z wyjatkiem gdy i =3
print(a)


#definicja fcji tokenize przyjmuje arg w postaci ciaglego tekstu w zmiennej text

def tokenize(text):
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text));
    words = [word for word in words if word not in cachedStopWords]
    tokens =(list(map(lambda token: PorterStemmer().stem(token),words)));
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token)>=min_length, tokens));
    return filtered_tokens


#    words = map(lambda word: word.lower(), word_tokenize(text));


#words to lista
#pojedynczy element tej listy to word
#wpd nalezy do listy words
#pod warunkiem ze word nie nalezy do listy cachedStopWords


#    p = re.compile('[a-zA-Z]+');


#    filtered_tokens = list(filter(lambda token: p.match(token) and len(token)>=min_length, tokens));



-------------



n = [3]
a = [(i,i*2) for i in range(6) if i not in n]
print(a)
#[(0, 0), (1, 2), (2, 4), (4, 8), (5, 10)]
#definicja funkcji tokenize, przyjmuje jeden argument w postaci ciągłego tekstu w zmiennej text
def tokenize(text):
    #definicja prostej zmiennej, przypisanie wartości 3 do min_length
    min_length = 3
    #word_tokenize - metoda z nltk, która zwraca poszatkowany tekst
    # "ala ma kota" -> ['ala','ma','kota']
    #lower - zamian dużych na małe litery
    # map - lambda expression, które wykonuje wszystkie operacje w pierwszym argumencie, aby utworzyć listę składającą się z elementów drugiego argumentu
    words = map(lambda word: word.lower(), word_tokenize(text));
    #words to lista
    #pojedynczym elementem tej listy jest word
    #word należy do listy words
    #pod warunkiem, że word nie należy do listy cachedStopWords
    words = [word for word in words if word not in cachedStopWords]
    # dla każdego elementu w words
    # wywal końcówkę, za pomocą PorterStemmer
    # i zapisz wynik na liście tokens
    tokens = (list(map(lambda token: PorterStemmer().stem(token), words)));
    #za pomocą biblioteki re tworzymy wzorzec (pattern) wyrażenia regularnego
    p = re.compile('[a-zA-Z]+');
    #znów tworzenie listy
    #każdy element listy musi być zgodny ze wzorcem p
    #długość elementu musi być większa niż min_length
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token)>=min_length, tokens));

pang sentiments set
http://www.cs.cornell.edu/people/pabo/movie-review-data/
polarity dataset v2.0 ( 3.0Mb) (includes README v2.0): 1000 positive and 1000 negative processed reviews. Introduced in Pang/Lee ACL 2004. Released June 2004.