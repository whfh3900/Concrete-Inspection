# -*- coding: utf-8 -*-
# model.py

# Copyright (c) 2018, Eric Liang Yang @chiyangliang@gmail.com
# Produced at the Robotics Laboratory of the City College of New York
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of the copyright holders nor the names of any
#   contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

## please switch to any model you prefer
import torch
from torch import nn
"""
from models import resnet as resnet
from models import vgg as resnet
from models.alexnet import *
"""

from models import resnet as resnet
#from models import *

def generate_model(opt):
    """
    if opt.model == 'resnet':
        from models import resnet
        model = resnet.resnet34(pretrained = True, num_classes=opt.n_classes)
    elif opt.model == 'vgg':
        from models import vgg
        model = vgg.vgg19(pretrained = True, num_classes=opt.n_classes)
    elif opt.model == 'alexnet':
        from models import alexnet
        model = alexnet.alexnet(pretrained = True, num_classes=opt.n_classes)
    elif opt.model == 'densenet':
        from models import densenet
        model = densenet.densenet169(pretrained = True, num_classes=opt.n_classes)
    elif opt.model == 'inception':
        from models import inception
        model = inception.inception_v3(pretrained = True, num_classes=opt.n_classes)
    elif opt.model == 'squeezenet':
        from models import squeezenet
        model = squeezenet.squeezenet1_1(pretrained = True, num_classes=opt.n_classes)
    else:
        print('Invalid model name')
    """
    model = resnet.resnet34(pretrained = True, num_classes=opt.n_classes)
    if not opt.no_cuda:
        model = model.cuda()
        model = nn.DataParallel(model, device_ids=None)

        if opt.pretrain_path:
            print('loading pretrained model {}'.format(opt.pretrain_path))
            pretrain = torch.load(opt.pretrain_path)
            assert opt.arch == pretrain['arch']

            model.load_state_dict(pretrain['state_dict'])

            return model, model.parameters()
    else:
        if opt.pretrain_path:
            print('loading pretrained model {}'.format(opt.pretrain_path))
            pretrain = torch.load(opt.pretrain_path)
            assert opt.arch == pretrain['arch']

            model.load_state_dict(pretrain['state_dict'])


            return model, model.parameters()

    return model, model.parameters()
