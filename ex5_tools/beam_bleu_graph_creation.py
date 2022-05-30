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


if __name__ == "__main__":
    create_beam_bleu_graph()
