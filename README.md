# MT Exercise 5: Byte Pair Encoding, Beam Search

# 2 Experiments with Byte Pair Encoding

# Changes

    Changes in config files for wordlvl, bpe2k, bpe5k
    Created new tools folder ex5_tools
    Added new scripts for working with the different configs
    
# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/gerie1/mt-exercise-5

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

    source venvs/torch3/bin/activate

Download and install required software:

    ./scripts/download_install_packages.sh

Download data:

    ./scripts/download_iwslt_2017_data.sh

The data is only minimally preprocessed, so you may want to tokenize it and apply any further preprocessing steps.

Choose data:
    
    We work with de-en.de and de-en.en

Sub-sample the training data randomly to 100k sentence pairs:

    ./scripts/sub_sample.sh

Tokenize data:

    ./scripts/tokenize_train.sh
    ./scripts/tokenize_test.sh
    ./scripts/tokenize_dev.sh

Create model/vocabulary of bpe 2k:

    ./scripts/create_model_bpe_2k.sh

Create model/vocabulary of bpe 5k:

    ./scripts/create_model_bpe_5k.sh

Train the models:

    ./scripts/train_wordlvl.sh
    ./scripts/train_bpe_2k.sh
    ./scripts/train_bpe_5k.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Evaluate the trained models with

    ./scripts/evaluate_wordlvl.sh
    ./scripts/evaluate_bpe_2k.sh
    ./scripts/evaluate_bpe_5k.sh

# Evaluation
