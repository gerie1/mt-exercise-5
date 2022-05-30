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

Translation Direction: DE - EN
Beam size: 5

|	|use BPE|vocabulary size|BLEU|
|:--:|:------:|:--------------:|:---:|
|(a)|no|2000|14.1|
|(b)|yes|2000|20.3|
|(c)|yes|5000|23.4|

We can see a clear difference when using BPE or not. When using a vocabulary size of 2000 (a) and (b) their is a big difference between the BLEU score. Only by using BPE in (b) we get an increase of almost 6 BLEU scores. And when using a bigger vocabulary size of 5000 the BLEU score increases to 23.4.

# Manual obeservations:

A big advantage of BPE over just doing the translation on the word level is that the <unk> label drops out and is replaced with a word. Which increases the fluency drastically.
But i found fascinating that BPE on 2000 vocab repeats some phrases with small changes sometimes e.g:
Robert Gupta: I want to play something that I would like to play something that I've been indeed.
BPE on 5000 vocab is more fluent in that sense.

# 3 Impact of beam size on translation quality

# Changes
    
Created .yaml files for different beam sizes and the corresponding evaluation script.
Added beam_bleu_graph_creation.py and a picture of the result Beam_BLEU_Graph.jpg.
    
![Beam_BLEU_Graph](https://user-images.githubusercontent.com/45572980/171043831-da506583-f919-4937-9ed6-4239e6c1cfcc.jpg)
    
# Findings

The BLEU score increases when the beam size gets bigger until it reaches a threshold.
BLEU increases from the beam size of 1 with 22.2 BLEU points to 23.4 (threshold) at a beam size of 5
After the threshold the score stagnates with increasing beam size until it sinks at a beam size of 16
In this case a big beam size produces roughly the same BLEU score but takes way longer to evaluate because
it has to take into the account of all the potential translation ways.
And a very small beam size is fast in evaluation but produces a low BLEU score.
In the future I would choose a beam size of 5 becauses it produces the highest BLEU score while evaluation takes
just a few minutes. This is a perfect balance between high BLEU score and runtime.

