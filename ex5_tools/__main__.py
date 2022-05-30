import argparse
from ex5_tools.sub_sample_data import sub_sample_data
from ex5_tools.tokenizer import tokenizer
from ex5_tools.beam_bleu_graph_creation import create_beam_bleu_graph


def main():
    ap = argparse.ArgumentParser("Ex5")

    ap.add_argument("--sub_sample", action="store_true",
                    help="Sub-sample the data")

    ap.add_argument("--tokenize", type=str, choices=['test', 'dev', 'train'], default="train",
                    help="Tokenize the test or dev or train dataset")
    
    ap.add_argument("--create_beam_bleu_graph", action="store_true",
                     help="Creates a beam size BLEU line graph")

    args = ap.parse_args()

    if args.sub_sample:
        print("Create sub-sample data")
        sub_sample_data()
        print("FINISHED")
    elif args.tokenize:
        print("Tokenization begins...")
        tokenizer(type=args.tokenize)
        print("FINISHED")
    elif args.create_beam_bleu_graph:
        print("Creating the graph")
        create_beam_bleu_graph()
        print("The graph was saved in your folder.")
    else:
        raise ValueError("Unknown mode")


if __name__ == "__main__":
    main()
