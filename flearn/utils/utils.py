import pickle
import pandas as pd

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def iid_divide(l, g):
    num_elems = len(l)
    group_size = int(len(l)/g)
    num_big_groups = num_elems - g * group_size
    num_small_groups = g - num_big_groups
    glist = []
    for i in range(num_small_groups):
        glist.append(l[group_size*i:group_size*(i+1)])
    bi = group_size*num_small_groups
    group_size += 1
    for i in range(num_big_groups):
        glist.append(l[bi+group_size*i:bi+group_size*(i+1)])
    return glist

class History:
    def __init__(self, names_list):
        self.history = {}
        for name in names_list:
            self.history[name] = []
            
    def add_name(self, name):
        if name in self.history.keys():
            raise ValueError('Key already exists!')
        
        self.history[name] = []
        
    def update(self, value_list):
        for key, value in zip(self.history.keys(), value_list):
            self.history[key].append(value)
            
    def get_history(self, dataframe=True):
        if dataframe:
            return pd.DataFrame.from_dict(self.history)
        else:
            return self.history