import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def create_beam_bleu_graph():
    d = {"Beam Size": [1, 2, 3, 4, 5, 6, 8, 12, 14, 16],
         "BLEU": [22.2, 23, 23.2, 23.3, 23.4, 23.3, 23.3, 23.3, 23.3, 23.2]}
    df = pd.DataFrame(data=d)

    sns.set_theme(style="whitegrid")
    lineplot = sns.lineplot(data=df, x="Beam Size", y="BLEU")
    plot = lineplot.get_figure()
    plot.savefig("Beam_BLEU_Graph.jpg", dpi=100)
    plt.show()


from ex5_tools.beam_bleu_graph_creation import create_beam_bleu_graph

ap.add_argument("--create_beam_bleu_graph", action="store_true",
                     help="Creates a beam size BLEU line graph")


    elif args.create_beam_bleu_graph:
        print("Creating the graph")
        create_beam_bleu_graph()
        print("The graph was saved in your folder.")



if __name__ == "__main__":
    create_beam_bleu_graph()
