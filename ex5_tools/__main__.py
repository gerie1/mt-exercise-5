import argparse

from ex5_tools.sub_sample_data import sub_sample_data
from ex5_tools.tokenizer import tokenizer


def main():
    ap = argparse.ArgumentParser("Ex5")

    ap.add_argument("--mode", choices=["train", "test", "translate"],
                    help="train a model or test or translate")

    ap.add_argument("--config_path", type=str,
                    help="path to YAML config file")

    ap.add_argument("--ckpt", type=str,
                    help="checkpoint for prediction")

    ap.add_argument("--output_path", type=str,
                    help="path for saving translation output")

    ap.add_argument("--save_attention", action="store_true",
                    help="save attention visualizations")

    ap.add_argument("-t", "--skip_test", action="store_true",
                    help="Skip test after training")

    ap.add_argument("-n", "--nbest", type=int, default=1,
                    help="Display n-best candidates when translating")

    ap.add_argument("--sub_sample", action="store_true",
                    help="Sub-sample the data")

    ap.add_argument("--tokenize", type=str, choices=['test', 'dev', 'train'], default="train",
                    help="Tokenize the test or dev or train dataset")

    args = ap.parse_args()

    if args.mode == "train":
        train(cfg_file=args.config_path, skip_test=args.skip_test)
    elif args.mode == "test":
        test(cfg_file=args.config_path, ckpt=args.ckpt,
             output_path=args.output_path, save_attention=args.save_attention)
    elif args.mode == "translate":
        translate(cfg_file=args.config_path, ckpt=args.ckpt,
                  output_path=args.output_path,
                  n_best=args.nbest)
    elif args.sub_sample:
        print("Create sub-sample data")
        sub_sample_data()
        print("FINISHED")
    elif args.tokenize:
        print("Tokenization begins...")
        tokenizer(type=args.tokenize)
        print("FINISHED")
    else:
        raise ValueError("Unknown mode")


if __name__ == "__main__":
    main()
