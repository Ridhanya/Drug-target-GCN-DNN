import numpy as np
def ddi_drug_feature(drugbank_id_file,drugbank_info_file, feature_id_file):
    f1 = open(drugbank_id_file,'r')
    drug_dict = {} # to map integers to drugbank IDs
    i = 0
    for line in f1:
        drug_dict[i] = line.split()[0]
        i+=1
    no_of_drugs = i
    adj_matrix_ddi = np.zeros([no_of_drugs,no_of_drugs]) # adjacency matrix of DDI
    f2 = open(drugbank_info_file,'r')
    lines = f2.readlines()
    n = len(lines)
    temp_arr = {} # to store drugbank data
    for i in range(0,n,5):
        temp_arr[lines[i].rstrip()] = [lines[i+1].rstrip(),lines[i+3].rstrip(),lines[i+4].rstrip()]
    f1.close()
    f2.close()  
    for i in range(0,no_of_drugs):
        for j in range(0,no_of_drugs):
            if drug_dict[j] in temp_arr[drug_dict[i]][1]:
                adj_matrix_ddi[i][j] = 1
    f3 = open(feature_id_file,'r')
    feature_dict = {} # to map integers to feature IDs
    i = 0
    for line in f3:
        feature_dict[i] = line.split()[0]
        i+=1
    no_of_features = i
    f3.close()
    feature_drug = np.zeros([no_of_drugs,no_of_features]) # store feature values of drugs
    for q in range(0,no_of_features):
        for t in range(0,no_of_drugs):
            if feature_dict[q] in temp_arr[drug_dict[t]][0]:
                feature_drug[t][q] = 1
    return(adj_matrix_ddi,feature_drug,drug_dict)
    
