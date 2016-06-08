import pickle

words = []
pos = 0
foo = open("words.txt","r",1)
for line in foo:
    words.append(line)
foo.close()
pickle.dump(words, open("words.p","wb"))


