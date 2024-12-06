import numpy as np

def mask_to_adj(sen_sec_mask):
    sen_num = sen_sec_mask.shape[1]
    sec_num = sen_sec_mask.shape[0]
    adj = np.zeros((sen_num+sec_num, sen_num+sec_num))
    # section connection
    secs_mask = np.sum(sen_sec_mask, axis=1)
    secs_mask[secs_mask > 0] = 1
    secs_mask[-1] = 0
    print(secs_mask)
    adj[-sec_num:, 0:-sec_num] = sen_sec_mask
    adj[-sec_num:, -sec_num:] = secs_mask
    # adj[-sec_num:, -sec_num:] = 0
    #document connection
    adj[-1, -sec_num:] = 1
    adj[-1, :-sen_num] = 1
    #build sentence connection
    start = 0


    for i in range(0, sec_num):
        sec_mask = sen_sec_mask[i]

        sec_sen_num = int(np.sum(sec_mask))
        adj_sec = np.zeros((sec_sen_num, sen_num + sec_num))
        adj_sec[:, :sen_num] = sec_mask
        # adj_sec[:, :sen_num] = 1
        # adj_sec[:, sen_num + i] = 1
        adj_sec[:, -sec_num:-1] = secs_mask[:-1]
        adj_sec[:, -1] = 0

        adj[start: start + sec_sen_num, :] = adj_sec
        start += sec_sen_num
    return adj, sen_num, secs_mask
    
    

sen_sec_mask = np.array([[1, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 1]])
                
mask_to_adj(sen_sec_mask)