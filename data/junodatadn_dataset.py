import os.path
import torch, h5py
from data.base_dataset import BaseDataset
import numpy as np
import pandas as pd

class JUNOdataDNDataset(BaseDataset):
    def __init__(self, opt):
        BaseDataset.__init__(self, opt)
        self.opt = opt
        csvA_path= os.path.join(opt.dataroot, opt.phase) + 'A.csv'#dataroot/trainA.csv
        #csvB_path= os.path.join(opt.dataroot, opt.phase) + 'B.csv'
        self.h5A_path = os.path.join(opt.dataroot, opt.phase) + 'A.h5' #dataroot/trainA.h5
        self.h5B_path = os.path.join(opt.dataroot, opt.phase) + 'B.h5'
        self.h5Afile = h5py.File(self.h5A_path, 'r')
        self.h5Bfile = h5py.File(self.h5B_path, 'r')
        self.dn_img = np.load('/hpcfs/juno/junogpu/jiangw/Denoising/GNMD/P2P-DN/data/DNimg.npy')

        csv_info = pd.read_csv(csvA_path, header=None)
        self.groupname = np.asarray(csv_info.iloc[:,0])
        self.datainfo = np.asarray(csv_info.iloc[:,1])

    def __len__(self):
        return len(self.datainfo)

    def __getitem__(self, idx):
        dset_entryA = self.h5Afile[self.groupname[idx]][self.datainfo[idx]]
        dset_entryB = self.h5Bfile[self.groupname[idx]][self.datainfo[idx]]
        imgA = torch.from_numpy(np.concatenate([np.array(dset_entryA),self.dn_img])).to(torch.float32)
        imgB = torch.from_numpy(np.array(dset_entryB)).to(torch.float32)
        A_path = [self.h5A_path, self.groupname[idx], self.datainfo[idx]]
        B_path = [self.h5B_path, self.groupname[idx], self.datainfo[idx]]
        return {'A': imgA, 'B': imgB, 'A_paths': A_path, 'B_paths': B_path}


def test():
    dataset = JUNOdataDNDataset('mergeDefault.h5', 'csvDefault.csv')
    print(0, dataset[0][0].shape)

if __name__ == '__main__':
    test()
