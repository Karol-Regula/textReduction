#prepare text
iliad  = open("Iliad.txt", "r")
iliad = iliad.read()
iliad = iliad.split()
iliad = [x.translate(None, ".,!?()\'\"") for x in iliad]
iliad = [x.lower() for x in iliad]
#print iliad

#find frequency of word in text
def wordFreq(word):
  print "Frequency of the word \'" + word + "\':"
  return len(filter(lambda x: x == word.lower(), iliad))

print wordFreq("sleep")
print wordFreq("the")
print ''

#find frequency of group of words
def groupFreq(words):
  print "Frequency of the word(s) \'" + str(words) + "\':"
  return len(filter(lambda x: True if x in words else False, iliad))

words = ['we', 'run', 'now', 'food']
print groupFreq(words)
print ''

#find most common word
words = {}
def commonFreq():
  map(count, iliad)
  out = sorted(words.items(), key=lambda x: x[1])
  print out[-5]
  print out[-4]
  print out[-3]
  print out[-2]
  return out[-1]

def count(word):
  if word not in words.keys():
    words[word] = len(filter(lambda x: x == word.lower(), iliad))
    #print word + " : " + str(words[word])
    #print len(words.keys())
  return word

#print "len(iliad): " + str(len(iliad))
iliad = iliad[0:10000]

print "Only using first 10000 words of iliad for this one because it took too long."
print "This should take < 10 seconds."
print "Five most common words:"
print commonFreq()



#Assignment notes:
#get book from project gutenberg
#use map, filter and reduce to find:
#basic frequency of a single word
#frequency of a group of words, preopsitions, names
#most frequently occurring word, might be more than one map-reduce
