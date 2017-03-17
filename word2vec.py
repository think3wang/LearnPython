import gensim, logging
from gensim.models import Word2Vec

print "loading embeddings"
model = Word2Vec.load_word2vec_format('GoogleNews-model/GoogleNews-vectors-negative300.bin', binary=True)
print model['bash']
print len(model['bash'])
print len(model['trump'])
print 'haha, finished'
