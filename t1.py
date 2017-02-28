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
