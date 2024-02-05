import sys
import random
import os, copy, pickle, time
import argparse
import itertools
from collections import defaultdict, Counter, OrderedDict
import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns
import torch
import torchvision
from torch import optim, nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader
from torch.autograd import Variable
import pandas as pd

# sys.path.append('scripts')
from scripts import lms_utils
from scripts import data_utils as du
from scripts import gpu_utils as gu
from scripts import ptb_utils as pu
from scripts import synth_models
from scripts import gendata
from scripts import utils
from scripts import synth_models as sm
from scripts import mnistcifar_utils as mc_utils
from scripts import ensemble

torch.backends.cudnn.benchmark = True
torch.backends.cudnn.enabled = True

def get_data(**c):
    smargin = c['lin_margin'] if c['same_margin'] else c['slab_margin']
    data_func = gendata.generate_ub_linslab_data_v2
    spc = [3]*c['num_slabs3']+[5]*c['num_slabs'] + [7]*c['num_slabs7']
    data = data_func(c['num_train'], c['dim'], c['lin_margin'], slabs_per_coord=spc, eff_slab_margin=smargin, random_transform=c['random_transform'], N_te=c['num_test'],
                     corrupt_lin_margin=c['corrupt_lin_margin'], num_lin=c['num_lin'], num_slabs=c['num_slabs3']+c['num_slabs']+c['num_slabs7'], width=c['width'], bs=c['bs'], 
                     corrupt_lin=c['corrupt_lin'], corrupt_slab=c['corrupt_slab'], corrupt_slab7=c['corrupt_slab7'])
    return data
