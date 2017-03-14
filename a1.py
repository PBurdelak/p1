from os import listdir


class corpus:
    def __init__(self,dir_neg,dir_pos):
        self.dir_neg = dir_neg
        self.dir_pos = dir_pos
        self.documents = []
        for i, file in enumerate(listdir(dir_neg)):
            if i < 300:
                fs = open(dir_neg + "\\" + file, 'r')
                text = fs.read()
                positive = 0
                train = 0
                doc = document(text, positive, train)
                self.add_document(doc)
                # negdocs.append(open(dir_neg + "\\" + file,'r').read())
            else:
                fs = open(dir_neg + "\\" + file, 'r')
                text = fs.read()
                positive = 0
                train = 1
                doc = document(text, positive, train)
                self.add_document(doc)

            for i, file in enumerate(listdir(dir_pos)):
                if i < 300:
                    fs = open(dir_pos + "\\" + file, 'r')
                    text = fs.read()
                    positive = 1
                    train = 0
                    doc = document(text, positive, train)
                    self.add_document(doc)

                    # negdocs.append(open(dir_neg + "\\" + file,'r').read())
                else:
                    fs = open(dir_pos + "\\" + file, 'r')
                    text = fs.read()
                    positive = 1
                    train = 1
                    doc = document(text, positive, train)
                    self.add_document(doc)


    def add_document(self, document):
        self.documents.append(document)

    def get_train_documents(self):
        train = []
        for doc in self.documents:
            if doc.train == 1:
                train.append(doc.text)
        return train


    def initialize_vocalbulary(self):
        self.vocabulary = []
        self.inversevocabulary = []
        for i,doc in enumerate(self.documents):
            if i % 1000 == 0:
                print(i)
            for word in doc.get_unique_values():
                if word not in self.vocabulary:
                    self.vocabulary[i] = word
                    self.inversevocabulary[word] = i

class document:
    def __init__(self, text, positive =1 , train=1):
        self.positive = positive
        self.train = train
        self.text = text

    def get_unique_words(self):
        word_list=[]
        for word in self.text.split():
            if not word in word_list:
                word_list.append(word)
        return word_list

    def get_vector(self, inverse_vocabulary):
        lng = len(inverse_vocabulary)
        vector = [0 for i in range(lng)]
        for word in self.text.split():
            vector[inverse_vocabulary[word]] = 1
        return vector

crp = corpus("C:\\Users\\s0152854\\Downloads\\txt_sentoken\\neg","C:\\Users\\s0152854\\Downloads\\txt_sentoken\\pos")
crp.initialize_vocalbulary()
print(crp.vocabulary)
