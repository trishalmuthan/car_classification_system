import os
import scipy.io

#with open('class_names.txt', 'w') as f:
#    for folder in os.listdir("sorted_data\\train"): 
#        f.write(folder)
#        f.write('\n')

mat = scipy.io.loadmat('cars_meta.mat')
print(len(mat['class_names'][0]))
#mat2 = scipy.io.loadmat('cars_annos.mat')
#print(mat2)





