#
#  ENVISIoN
#
#  Copyright (c) 2018  Viktor Bernholtz
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import os, sys

# Configuration
PATH_TO_ENVISION=os.path.expanduser("~/ENVISIoN/envision")
PATH_TO_VASP_CALC=os.path.expanduser("~/ENVISIoN/examples/data/TiPO4")
PATH_TO_HDF5=os.path.expanduser("/tmp/envision_demo.hdf5")

sys.path.insert(0, os.path.expanduser(PATH_TO_ENVISION)) # Or `pip install --editable`.

import envision
import envision.inviwo
import envision.parser.vasp as parsers
import h5py

parsers.fermi_surface('/tmp/testfile.hdf5', '/home/viktor/ENVISIoN/data/TiPO4')

name_list = []
with h5py.File('/tmp/testfile.hdf5', 'r') as f:
    f.visit(name_list.append)
    print(f['FermiSurface/KPoints/18/Coordinates'][2])

#print(name_list)