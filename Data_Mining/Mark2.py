from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np
import Mark1
import Mark3
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def calcSSE(n_clusters, labels, indices, listTFIDF):
    
    print len(labels)
    print len(indices)
    centList = []
    listCluster = []
    for i in range(n_clusters):
        listCluster.append(set({}))
    for i in range(0,len(labels)):
        listCluster[labels[i]].add(indices[i])
#    print "hi"
    centList = Mark3.updatedCentriods(listCluster,listTFIDF)
    SSE = Mark3.calculateSSE(centList, listCluster, listTFIDF)
    print SSE
# Compute DBSCAN
def calcDBScan(listTFIDF):
    x = []
    try:
        for i in range (0,len(listTFIDF)):
            temp = []
            for j in range(0,len(listTFIDF)):
                dist = Mark3.getDistance(listTFIDF[i],listTFIDF[j])
                dist = dist
                temp.append(dist)
            x.append(temp)
        
        
        standardScale = StandardScaler().fit_transform(x)
        db = DBSCAN(eps=0.6, min_samples=1).fit(standardScale)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        
        labels = db.labels_
        n_clusters_ = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
        calcSSE(n_clusters_, labels,db.core_sample_indices_,listTFIDF)
        
        
    except:
        print "Exception Here"