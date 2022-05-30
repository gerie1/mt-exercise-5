#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

tools=$base/tools
mkdir -p $tools

echo "Make sure this script is executed AFTER you have activated a virtualenv"

# manually install some joeynmt dependencies 
# reason: joeynmt uses torchtext.legacy.data.Dataset, which has been removed from torchtext >= 0.12
# see https://github.com/joeynmt/joeynmt/issues/158 (comments at the bottom) 

pip uninstall setuptools
pip install setuptools==59.5.0
# Can only download torchtext==0.12 when Python version 3.10 -> Had to downgrade to version 3.8
#ERROR: Could not find a version that satisfies the requirement torchtext==0.11.2 (from versions: 0.1.1, 0.2.0, 0.2.1, 0.2.3, 0.3.1, 0.4.0, 0.5.0, 0.6.0, 0.12.0)
pip install torchtext==0.11.2
pip install spacy
pip install protobuf==3.19.4

# install joeynmt (installs subword-nmt in the process)

git clone https://github.com/joeynmt/joeynmt.git $tools/joeynmt

(cd $tools/joeynmt && pip install .)

# install Moses scripts for preprocessing

git clone https://github.com/bricksdont/moses-scripts $tools/moses-scripts
