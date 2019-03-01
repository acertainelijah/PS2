import math
import os
from nltk.stem import PorterStemmer
import xml.etree.ElementTree as ET
# Documents to search through
d = []
#d.append("jack and jill went up the hill")
d.append("jack jill went up hill")
d.append("to fetch a pail of water")
d.append("jack fell down and broke his crown")
d.append("and jill came tumbling after")
d.append("up jack got and home did trot")
d.append("as fast as he could caper")
d.append("to old dame dob who patch his nob")
d.append("with vinegar and brown paper")

k_freq = []
k_freq.append(0)

# Query to search in document
q = "jack"

# D is the array of all words in all documents
D_n = 39
D = []
D.append("jack")
D.append("and")
D.append("jill")
D.append("went")
D.append("up")
D.append("the")
D.append("hill")
D.append("to")
D.append("fetch") 
D.append("a")	
D.append("pail")
D.append("of")	
D.append("water")	
D.append("fell")	
D.append("down")	
D.append("broke")	
D.append("his") 	
D.append("crown")	
D.append("came")	
D.append("tumbling")	
D.append("after")	
D.append("got")	
D.append("home")	
D.append("did")	
D.append("trot")	
D.append("as") 	
D.append("fast")	
D.append("he")
D.append("could")	
D.append("caper")	
D.append("dame")	
D.append("dob")	
D.append("who")	
D.append("patched")	
D.append("nob")	
D.append("with")	
D.append("vinegar")	
D.append("brown")	
D.append("paper")

# q_i
Q_arr = [0] * 39
Q_arr[0] = 1




## TF-IDF
def term_frequency(term, d):
	k = 0
	freq = 0
	k_freq = []
	k_freq.append(0)
	document = d[k]
	numWords = 0

	for word in document.split():
		numWords += 1
		if (word == term):
			freq += 1

	## print "\t" + str(freq) + " occurrences of term \'" + term + "\'' in the document."

 	total_freq = 0
 	k_freq_set = False
	for docs in d:
		k_freq_set = False
		for word in docs.split():
			if (word == term):
				total_freq += 1
				if (k_freq_set == False):
					k_freq[0] = k_freq[0] + 1
					k_freq_set = True
					## print "\tk_freq: " + str(k_freq[0])

	freq = float(freq) / numWords
	tf = freq
	#tf = float(freq) / total_freq
	#print "\ttf = " + str(freq) + " / " + str(total_freq)
	print "\ttf = " + str(tf)
	## print "\t" + "total_freq " + str(total_freq)
	## print  str(tf) + " is the term frequency weight of term \'" + term + "\'' in document" + d[k]
	## print "\tkfreq before return : " + str(k_freq[0])
	## return tf
	IDF = idf(len(d), k_freq[0])
	print "\tidf = " + str(IDF)
	w = tf * IDF
	print "w = tf * idf for term: " + str(term)
	print str(w) + " = " + str(tf) + " * " + str(IDF)



def idf(N, n_k):
	print "\t\tN = " + str(N)
	print "\t\tn_k = " + str(n_k)
	if n_k != 0:
		df = float(N) / n_k
		print "\t\tN / n_k = " + str(df)
		if df > 0: 
			#idf = math.log( df , 2 )
			idf = math.log10(df)
			return idf
		else:
			return 9999	
	else:
		return 9000		

## Vector Space Model

def binary_summation(q_i, d_i):
	product = 0
	for i in xrange(len(d_i)):
		product += q_i[i] * d_i[i]
	return product 

def inner_product(q,d):
	doc_num = 1
	for document in d:
		d_arr = [0] * 39
		product = 0
		for i in xrange(len(D)):
			if (D[i] in document):
				d_arr[i] += 1

		product = binary_summation(Q_arr, d_arr)
		print "d" + str(doc_num) + " inner product: " + str(product)
		doc_num += 1	


def cos_sim(q,d):
	doc_num = 1
	for document in d:
	#for k in xrange(len(d)):	
		d_arr = [0] * 39
		product = 0
		for word in document.split():
			for i in xrange(len(D)):
			# print "i: " + str(i) + " D_i: " + D[i]
				if (word == D[i]):
					d_arr[i] += 1
					#print "D: " + D[i] + "\t" + "d_arr[" + str(i) +"]: " + str(d_arr[i])
				#print "\tword: " + str(word)
				#print "\tD[" + str(i) + "]: " + str(D[i])
					

		product = binary_summation(Q_arr, d_arr)
		Q_sqrt = math.sqrt(binary_summation(Q_arr, Q_arr))
		D_sqrt = math.sqrt(binary_summation(d_arr, d_arr))

		#print "d" + str(doc_num) + " inner product: " + str(product)
		#print "\td" + str(doc_num) + " Q_sqrt: " + str(Q_sqrt)
		#print "\td" + str(doc_num) + " D_sqrt: " + str(D_sqrt)

		end_product = product / (Q_sqrt * D_sqrt)

		print "d" + str(doc_num) + " cos sim: " + str(end_product)
		doc_num += 1
	print"\n"
	

class termInfo:
	num_docs = 0
	postings = {}

class docIndex:
    # List of words that contains dictionaries of (#docs, liked list of postings tuples)
	word_indx = {}
	doc_indx = {}

def docFreq(currr_term, currr_file_name):
	print("docFreq: " + currr_term)
	tottt_terms = 0
	print "gonna loop"
	print "file this : "
	file = open(currr_file_name, "r")
	#print file
	for werd in file.read().split():
		#print "curr line word: " + werd
		new_werd = werd.lower()
		if currr_term == new_werd:
			tottt_terms += 1
	print "doc freq (" + str(currr_term) + "): " + str(tottt_terms)
	return tottt_terms

def isClean(word):
	if 'http' in word or not word.isalpha():
		#print "\t" + word + " is NOT clean"
		return False
	else:
		#print word + " is clean!!!"
		return True

## Main
inner_product(q,d)
print "\n"
cos_sim(q,d)
print "\n"


## TF-IDF for terms in D_1 in hw
d1 = d[0]
for word in d1.split():
	tf = term_frequency(word, d)
	k_f = k_freq[0]
	#print "\tbefore tf k_freq: " + str(k_f)
	len_d = len(d)
	#idf = idf(len_d, int(k_f))
	#IDF = idf(len_d, 10)
	#w = tf * IDF
	#print "w = tf * idf"
	#print str(w) + " = " + str(tf) + " * " + str(IDF)


## create word and posting index
test = docIndex()

# get stop words
stop_words = []
with open('stoplist.txt','r') as f:
    for line in f:
        for word in line.split():
           stop_words.append(word)

# Parse out the ap89_collection
dict_of_files = {}
print "about to et  mmmm"
tree = ET.parse('./data/ap89_collection.xml')
root = tree.getroot()
for doc in root.findall(('doc')):
	docid = doc.find('docno').text
	#print("docid " + str(docid))
	text = doc.find('text').text
	#print("text " + str(text))
	dict_of_files[docid] = text

print dict_of_files
# do indexing
# path = "./data/"
# ignored = {".DS_Store"}
# list_of_files = [x for x in os.listdir(path) if x not in ignored]
# for i in xrange(len(list_of_files)):
# 	list_of_files[i] = path + list_of_files[i]
# print list_of_files
# #doc_i = 1
# for doc_i in xrange(1, len(list_of_files)):
# 	num_words = 0
# 	print "Current doc_i ^^^: " + str(doc_i)
# 	print "List of files curr ^^^: " + str(list_of_files[doc_i])
# 	with open(list_of_files[doc_i], 'r') as f:
# 		for line in f:
# 			for word in line.split():
# 				# Apply stemming
# 				ps = PorterStemmer()
# 				new_word = word.lower()
# 				new_word = ps.stem(new_word)
# 				print "cuurr new_wrod uWu: " + new_word
# 				if new_word not in stop_words and isClean(new_word):
# 					num_words += 1
# 					print("word: " + str(new_word) + " doc_i = " + str(doc_i)) # Apply stemming!
# 					if new_word in test.word_indx:  # Add to Word Index + Document Index
# 						print "word exists"
# 						test.word_indx[new_word].num_docs += 1
# 						temp_doc_freq = docFreq(new_word, list_of_files[doc_i])
# 						test.word_indx[new_word].postings[doc_i] = temp_doc_freq
# 					else:
# 						print "word (" + new_word + ") does not exist"
# 						info = termInfo() # add posting info
# 						info.num_docs = 1
# 						test.word_indx[new_word] = info
# 						test.word_indx[new_word].postings[doc_i] = docFreq(new_word, list_of_files[doc_i])
#
# 	test.doc_indx[doc_i] = num_words  # add to doc index
#
#
#
# print "DONE!!!"
#
# print "test.word_indx:"
# print test.word_indx
# for element in test.word_indx:
# 		print element, test.word_indx[element].num_docs, test.word_indx[element].postings
#
# print
# print "test.doc_indx"
# print test.doc_indx
# TODO Parse the ap89_collection, then query
