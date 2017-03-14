#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gensim, logging
from gensim.models import word2vec
import sys
import string, codecs
import numpy as np
import math

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
argvs = sys.argv;  argc = len(argvs)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec.load("dena.model")
voc = model.wv.vocab.keys()
outf = codecs.open('dena_vector.csv', 'w', encoding='utf-8')

for x in voc:
  try:
     wvec = model[x]
  except KeyError:
     print (x, u'を無視します')
  outf.write('"' + x + '"' + ', ' )
  c = 0
  for v in wvec:
     if c==0:
        outf.write(str(v))
     else:
        outf.write(', '+str(v))
     c += 1
  outf.write('\n')
outf.close()