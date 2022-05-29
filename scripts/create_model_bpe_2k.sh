#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data
tools=$base/tools

mkdir -p $base/shared_models/
shared_models=$base/shared_models/



subword-nmt learn-joint-bpe-and-vocab \
--input $data/train.de-en-sample-tokenized.de $data/train.de-en-sample-tokenized.en \
--write-vocabulary $shared_models/vocab-2k.src $shared_models/vocab-2k.trg \
-s 2000 --total-symbols -o $shared_models/model2k.bpe

subword-nmt apply-bpe -c $shared_models/model2k.bpe \
--vocabulary $shared_models/vocab-2k.src \
--vocabulary-threshold 10 \
< $data/train.de-en-sample-tokenized.de > $data/train.de-en-sample-tokenized-bpe-2k.de

subword-nmt apply-bpe -c $shared_models/model2k.bpe \
--vocabulary $shared_models/vocab-2k.src \
--vocabulary-threshold 10 \
< $data/dev.de-en-tokenized.de > $data/dev.de-en-tokenized-bpe-2k.de

subword-nmt apply-bpe -c $shared_models/model2k.bpe \
--vocabulary $shared_models/vocab-2k.src \
--vocabulary-threshold 10 \
< $data/test.de-en-tokenized.de > $data/test.de-en-tokenized-bpe-2k.de

subword-nmt apply-bpe -c $shared_models/model2k.bpe \
--vocabulary $shared_models/vocab-2k.trg \
--vocabulary-threshold 10 \
< $data/train.de-en-sample-tokenized.en > $data/train.de-en-sample-tokenized-bpe-2k.en

subword-nmt apply-bpe -c $shared_models/model2k.bpe \
--vocabulary $shared_models/vocab-2k.trg \
--vocabulary-threshold 10 \
< $data/test.de-en-tokenized.en > $data/test.de-en-tokenized-bpe-2k.en

subword-nmt apply-bpe -c $shared_models/model2k.bpe \
--vocabulary $shared_models/vocab-2k.trg \
--vocabulary-threshold 10 \
< $data/dev.de-en-tokenized.en > $data/dev.de-en-tokenized-bpe-2k.en

python3 $tools/joeynmt/scripts/build_vocab.py \
$data/train.de-en-sample-tokenized-bpe-2k.de $data/train.de-en-sample-tokenized-bpe-2k.en \
--output_path $shared_models/vocab-2k.txt