import os

path = '/media/samvel/Storage/FIlms/'

for s in range(1, 8):
    os.makedirs(path + f'{s} сезон', exist_ok=True)