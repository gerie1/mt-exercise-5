import random
import os


def sub_sample_data():
    # Generate random number sample
    rand_num_list = random.sample(range(209522), 100000)

    # Initiate paths
    new_path_de = "data/train.de-en.de"
    new_path_en = "data/train.de-en.en"

    new_path_de_sample = "data/train.de-en-sample.de"
    new_path_en_sample = "data/train.de-en-sample.en"

    # Create sub sample data
    with open(new_path_de, "r", encoding="utf-8") as de_file, open(new_path_en, "r", encoding="utf-8") as en_file:
        de_data = de_file.readlines()
        en_data = en_file.readlines()
        with open(new_path_de_sample, "w", encoding="utf-8") as de_sample, open(new_path_en_sample, "w", encoding="utf-8") as en_sample:
            for randnr in rand_num_list:
                de_sample.write(de_data[randnr])
                en_sample.write(en_data[randnr])


if __name__ == '__main__':
    sub_sample_data()

