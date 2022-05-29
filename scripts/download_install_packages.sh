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
pip install torchtext==0.11.2
pip install spacy

# install joeynmt (installs subword-nmt in the process)

git clone https://github.com/joeynmt/joeynmt.git $tools/joeynmt

(cd $tools/joeynmt && pip install .)

# install Moses scripts for preprocessing

git clone https://github.com/bricksdont/moses-scripts $tools/moses-scripts
