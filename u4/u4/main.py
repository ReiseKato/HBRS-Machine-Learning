import os
from scipy.spatial.distance import squareform
from util import *

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'blogdata.json')
    df = load_data(file_path)

    word_freqs = df.drop(columns=['Blog'])
    transposed_df = word_freqs.T
    distances = pdist(transposed_df, metric='correlation')
    linkage_matrix = linkage(distances, method='average')

    plt.figure(figsize=(len(word_freqs), 12))
    dendrogram(linkage_matrix, labels=transposed_df.index, leaf_rotation=90)
    plt.title("Hierarchisches Clustering der Wörter (Pearson)")
    plt.xlabel("Wort")
    plt.ylabel("1 - Pearson-Korrelation")
    plt.tight_layout()
    plt.savefig(r'u4\results\dendogram_words.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()