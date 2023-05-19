import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def main():
    docs = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    query = np.array([1,1,0,0,1,0])
    doc1 = cosine_similarity([docs[0]],[query])
    doc2 = cosine_similarity([docs[1]],[query])
    doc3 = cosine_similarity([docs[2]],[query])

    print("doc1=", np.around(doc1[0][0],decimals=2))
    print("doc2=", np.around(doc2[0][0],decimals=2))
    print("doc3=", np.around(doc3[0][0],decimals=2))
    
if __name__ == '__main__':
    main()
