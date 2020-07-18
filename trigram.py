from trigram.trigram_model import *

def load(path):
    all_lines = []
    with open(path, encoding="UTF-8") as file:
        all_lines = file.read().replace("\n", " ")
    return all_lines


def addInOrAddOut(dictionary, word, otherWord):
    if word in dictionary:
        dictionary[word].append(otherWord)
    else:
        dictionary[word] = [otherWord]


def clean_sentence(sentence):
    sentence = [clean_word(word) for word in sentence]
    if "" in sentence:
        sentence.remove("")
    return sentence


def clean_word(word):
    unwanted = {",", ":", "\\", "/", "\"", "\'", "\’", " ", ";",
                "“", "*", "”", "“", "\t", "\r", "2X.", "2x.", "4X.","4x.", "2X", "2x", "4x", "4X"}
    for x in unwanted:
        if x in word:
            word = word.replace(x, "")
    return word


class Trigram:
    def __init__(self):
        self.model = Trigram_model()
        self.allLines = ""

    ##can be called multiple times filles trigram model with data from a file
    ##more loads from different files, bigger base to calculate words
    def load_from_file(self, path):
        all_lines = load(path)
        self.allLines += all_lines
        self.build_model()

    def build_model(self):
        for sentence in self.allLines.split("."):
            self.sentence_to_model(clean_sentence(sentence.split(" ")))

    def sentence_to_model(self, sentence):
        curr_node = self.model.starting_node
        for index, word in enumerate(sentence):
            if index==0:
                curr_node = curr_node.add_and_return_child_by_name((".", word))
            elif index==len(sentence):
                curr_node = curr_node.add_and_return_child_by_name((".", "."))
            else:
                curr_node = curr_node.add_and_return_child_by_name((sentence[index-1], word))


    # runs throught the created model and makes sentences
    def create_text(self, number_of_words):
        curr_node = self.model.starting_node
        counter = 0
        line_length = 0
        while counter<number_of_words:
            curr_node = curr_node.get_random_child()
            word = curr_node.name[1]
            if word == ".":
                print(word, end="")
                continue
            print(" " + word, end = "")

            line_length += len(curr_node.name[1])
            counter+=1
            if line_length > 100:
                print("")
                line_length = 0

if __name__ == '__main__':
    gram = Trigram()
    gram.load_from_file("test.txt")
    gram.create_text(500)
