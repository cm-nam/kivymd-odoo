import pickle

def save_pickle_data(data):
    with open("data.txt", "wb") as f:
        f.write(pickle.dump(data))
