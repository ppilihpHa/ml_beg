import pandas as pd
import numpy as np

# get Src
df = pd.read_json(r"C:\Users\phili\OneDrive\Dokumente\Uni\Sem_3\Python\prv\ml\ml_beg\firstSrc.json", orient="records", lines=True)

ary = df.values

l = [[1,2,3],[4,5,6],[7,8,9]]
ary2 = np.array(l)

vector_ary2 = ary2.reshape(9) # very different to (9,1) --> if not sure use -1 for numpy to fill in
ndim_ary2 = ary2.reshape(3,3,1)
arry_new = vector_ary2.reshape(-1, 3) # get back 3 columns but dont know how many rows needed

# output --------------------------------------------------------------

#print(df.head(4))
#print(ary[:4,1])
#print(ary2)
#print(ary2.shape)
#print(vector_ary2)
#print(vector_ary2.shape)
#print(ndim_ary2)
#print(ndim_ary2.ndim, ndim_ary2.shape)
print(arry_new)
print(arry_new.shape)

# ---------------------------------------------------------------------