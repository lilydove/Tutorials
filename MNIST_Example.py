# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 06:37:04 2017

@author: Administrator
"""

from neon.backends import gen_backend
from neon.data import MNIST

be = gen_backend(batch_size=128)
mnist = MNIST(path='data/')
train_set = mnist.train_iter
valid_set = mnist.valid_iter
