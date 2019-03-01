# PS2

# Description
This Problem Set 2 extends Problem Set 1 by: 
1) supporting for complex queries using the Vector Space Model 
2) utilize stemming and stop words
3) evaluates various retrieval methods based on speed as well as Precision/Recall

# How To Run
  `python VectorSpaceModel.py`
  
# Structure
 We first get the needed stop words to ignore and put that into a list.
 We then iterate through ap89_collection to get the "docno" and "text"
 Once we get the text from each document, we then start tokenizing and indexing the words. (Stemming is applied)
 We then return postings by term, using the "returnPosting(term)" method.
 I now need to make sure to execute query. I need to read through the query results and output correct query results.
 I then would have to take those queries, and the results and run them through trec_eval
 
