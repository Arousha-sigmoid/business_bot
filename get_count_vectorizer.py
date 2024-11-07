#from sklearn.feature_extraction.text import CountVectorizer
#import pickle
import json

qna = json.load(open("qna.json",'rb'))
query_lis = [qset['query'] for qset in qna]

# count tokenizer
#tokenizer = CountVectorizer(ngram_range=(1,2))
#tok_arr = tokenizer.fit_transform(query_lis).toarray()
#tok_arr

#with open('query_tokenized.pkl','wb') as f:
#    pickle.dump(tok_arr,f)
#with open("tokenizer.pkl",'wb') as f:
#    pickle.dump(tokenizer,f)
# with open('query_tokenized.pkl','rb') as f:
#     q_toks = pickle.load(f)    