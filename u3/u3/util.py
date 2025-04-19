import os
import json
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

DEBUG = False

def load_data(filepath):
    data = None
    with open(filepath, 'r') as file:
        data = json.load(file)
    data = pd.DataFrame(data).T
    data.index.name = 'Blog'
    data.reset_index(inplace=True)

    if DEBUG: print(data)

    return data
    
def pearson_correlation_coefficient(x, y):
    '''
    Computes the Pearson correlation coefficient between two arrays x and y.
    The Pearson correlation coefficient is a measure of the linear correlation between two variables.
    '''

    # initialize x and y as numpy arrays
    x = np.array(x)
    y = np.array(y)

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    numerator = np.sum((x - mean_x) * (y - mean_y))
    dominator = np.sqrt(np.sum((x - mean_x) ** 2) * np.sum((y - mean_y) ** 2))

    if dominator == 0:
        return 0
    
    return numerator / dominator

def compute_distance_matrix(data):
    '''
    Computes the distance matrix for the given data using the Pearson correlation coefficient.
    The distance is defined as 1 - Pearson correlation coefficient.
    '''
    num_blogs = len(data)
    blogs = data["Blog"].tolist()
    if DEBUG: print(blogs)
    word_freqs = data.drop(columns=['Blog'])
    distances = np.zeros((num_blogs, num_blogs))

    for i in range(num_blogs):
        for j in range(i, num_blogs):
            blog_x = word_freqs.iloc[i].values
            blog_y = word_freqs.iloc[j].values
            distances[i][j] = distances[j][i] = 1 - pearson_correlation_coefficient(blog_x, blog_y)

    return pd.DataFrame(distances, index=blogs, columns=blogs)







def main_scipy():
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'blogdata.json')
    df = pd.read_json(file_path).T
    df.index.name = 'Blog'
    df.reset_index(inplace=True)
    print(df)

    word_freqs = df.drop(columns=['Blog'])

    distances = pdist(word_freqs, metric='correlation') # Compute pairwise distances using correlation metric (same as 1 - Pearson correlation) -> 1- pearsonr(x, y)[0] for all x, y blog pairs

    linkage_matrix = linkage(distances, method='average')

    plt.figure(figsize=(15, 8))
    dendrogram(linkage_matrix, labels=df['Blog'].values, leaf_rotation=90)
    plt.title('Hierarchisches Clustering der Blogs (Pearson)')
    plt.xlabel('Blog')
    plt.ylabel('1 - Pearson-Korrelation')
    plt.tight_layout()
    plt.savefig(r'u3\results\dendogram_scipy.png', dpi=300, bbox_inches='tight')
    plt.show()
