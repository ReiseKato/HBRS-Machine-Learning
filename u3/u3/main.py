import os
from scipy.spatial.distance import squareform
from util import *

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'blogdata.json')
    df = load_data(file_path)

    # Hierarchical clustering using Pearson correlation
    distance_df = compute_distance_matrix(df)
    condensed_distances = squareform(distance_df.values)
    linkage_matrix = linkage(condensed_distances, method='average')

    plt.figure(figsize=(16, 10))
    dendrogram(linkage_matrix, labels=distance_df.index.tolist(), leaf_rotation=90)
    plt.title("Custom Hierarchical Clustering")
    plt.xlabel("Blogs")
    plt.ylabel("Distance")
    plt.tight_layout()
    plt.savefig(r'u3\results\dendogram.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()