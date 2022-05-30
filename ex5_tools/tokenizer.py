import spacy
from spacy import cli


def tokenizer(type):
    spacy.cli.download("en_core_web_sm")
    spacy.cli.download("de_core_news_sm")
    nlp_en = spacy.load("en_core_web_sm")
    nlp_de = spacy.load("de_core_news_sm")

    if type == "train":
        filepath_input_en = "data/train.de-en-sample.en"
        filepath_input_de = "data/train.de-en-sample.de"
        filepath_output_en = "data/train.de-en-sample-tokenized.en"
        filepath_output_de = "data/train.de-en-sample-tokenized.de"
    elif type == "test":
        filepath_input_en = "data/test.de-en.en"
        filepath_input_de = "data/test.de-en.de"
        filepath_output_en = "data/test.de-en-tokenized.en"
        filepath_output_de = "data/test.de-en-tokenized.de"
    elif type == "dev":
        filepath_input_en = "data/dev.de-en.en"
        filepath_input_de = "data/dev.de-en.de"
        filepath_output_en = "data/dev.de-en-tokenized.en"
        filepath_output_de = "data/dev.de-en-tokenized.de"
    else:
        exit()

    with open(filepath_input_en, "r", encoding="utf-8") as en_f, open(filepath_input_de, "r", encoding="utf-8") as de_f:
        en_sample = en_f.readlines()
        de_sample = de_f.readlines()

        with open(filepath_output_en, "w", encoding="utf-8") as en, open(filepath_output_de, "w",
                                                                         encoding="utf-8") as de:
            for sent1 in en_sample:
                sentence_en = []
                doc = nlp_en(sent1)
                for token1 in doc:
                    sentence_en.append(token1.text)
                print(sentence_en)
                en.write(" ".join(sentence_en)[:-2])
                en.write("\n")

            for sent2 in de_sample:
                sentence_de = []
                doc = nlp_de(sent2)
                for token2 in doc:
                    sentence_de.append(token2.text)
                print(sentence_de)
                de.write(" ".join(sentence_de)[:-2])
                de.write("\n")


if __name__ == '__main__':
    tokenizer()
