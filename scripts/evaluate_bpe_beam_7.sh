#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data
configs=$base/configs

translations=$base/translations

mkdir -p $translations

src=de
trg=en

# cloned from https://github.com/bricksdont/moses-scripts
MOSES=$base/tools/moses-scripts/scripts

num_threads=4
device=0

# measure time

SECONDS=0

model_name=transformer_model_bpe_beam_7

echo "###############################################################################"
echo "model_name $model_name"

translations_sub=$translations/$model_name

mkdir -p $translations_sub

CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python -m joeynmt translate $configs/$model_name.yaml < $data/test.de-en-tokenized-bpe-5k.$src > $translations_sub/test.de-en-tokenized-bpe-5k.$model_name.$trg

# undo BPE

cat $translations_sub/test.de-en-tokenized-bpe-5k.$model_name.$trg | sed 's/\@\@ //g' > $translations_sub/test.de-en-tokenized-5k.$model_name.$trg

# undo tokenization

cat $translations_sub/test.de-en-tokenized-5k.$model_name.$trg | $MOSES/tokenizer/detokenizer.perl -l $trg > $translations_sub/test.de-en-detokenized-5k.$model_name.$trg

# compute case-sensitive BLEU on detokenized data

cat $translations_sub/test.de-en-detokenized-5k.$model_name.$trg | sacrebleu $data/test.de-en.$trg


echo "time taken:"
echo "$SECONDS seconds"
