from test import tf_idf
from test import feature_values
from os import listdir


class corpus:
    def __init__(self,dir_neg,dir_pos):
        self.dir_neg = dir_neg
        self.dir_pos = dir_pos

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
                    fs = open(dir_neg + "\\" + file, 'r')
                    text = fs.read()
                    positive = 1
                    train = 1
                    doc = document(text, positive, train)
                    self.add_document(doc)

        self.document = []
    def add_document(self,document):
        self.document.append(document)


class document:
    def __init__(self, text, positive =1 , train=1):
        self.positive = positive
        self.train = train
        self.text = text

crp = corpus("C:\\Users\\s0152854\\Downloads\\txt_sentoken\\neg","C:\\Users\\s0152854\\Downloads\\txt_sentoken\\pos")