import networkx as nx
from networkx.classes import function as fn
from networkx.algorithms import approximation as appr
from networkx.algorithms import assortativity as assrt
from networkx.algorithms import efficiency_measures as eff
from networkx.algorithms import components as comp
from networkx.algorithms import centrality as ctr
from networkx.algorithms import shortest_paths as shp

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import random as rdm

def plot_hist(values, ax, name='', title='', xlab='', ylab='Frecuencia', nbins=100):

    ax.set_title(title)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)

    ax.set_yscale('log')
    
    ax.hist(values, bins=np.arange(min(values), max(values), nbins))

    plt.savefig(name + '.png')


mal1 = '172.16.253.132'
mal2 = '192.168.248.165'

conn_df = pd.read_csv(
    'traffic/res/ISCX_Botnet-Testing.csv',
    header = None,
    error_bad_lines = False,
    names = ['source', 'target']
)

conn_weighted_df = conn_df.groupby(
    ['source', 'target']
    ).size().reset_index(name='weight')

N = nx.convert_matrix.from_pandas_edgelist(
    conn_weighted_df,
    edge_attr='weight'
    )
N.name = 'ISCX Botnet'

print(fn.info(N))
print('Connected components: ', comp.number_connected_components(N))

n1 = comp.node_connected_component(N, mal1)
n2 = comp.node_connected_component(N, mal2)

I = N.subgraph(n1.union(n2))
I.name = 'Induced Botnet'
print(fn.info(I))

#nx.draw(I, label = 'ISCX Botnet 2014, 25%', with_labels = False, font_size = 5, node_size = 0.5)
#plt.title(N.name)

fig, axs = plt.subplots(1, 1)


h1 = [d for n, d in I .degree()]
plot_hist(h1, axs, name='cgrad',title='Centralidad de grado',
 xlab='Fracción del grado máximo')


h2 = assrt.average_neighbor_degree(I).values()
plot_hist(h2, axs, name='cavgnei', title='Grado promedio de vecinos', xlab='Grado promedio')


h3 = ctr.information_centrality(I).values()
plot_hist(h3, axs, name='cinfo', title='Centralidad de información',
 xlab='Flujo de información')

h4 = ctr.closeness_centrality(I).values()
plot_hist(h4, axs, name='cclose', title='Centralidad de cercanía',
 xlab='Inverso de distancia promedio')

h5 = ctr.betweenness_centrality(I).values()
plot_hist(h5, axs, name='cbetw', title='Centralidad de intermediario',
xlab='Fracción de rutas pasantes')

h6 = ctr.eigenvector_centrality(I).values()
plot_hist(h5, axs, name='ceigen', title='Centralidad de valores propios',
xlab='Centralidad de los vecinos')

print('Clustering coefficient: {0:.4f}'.format(
    appr.clustering_coefficient.average_clustering(N)
    )
)

print('Average distance:', shp.average_shortest_path_length(I))

print('Connectivity: ', appr.node_connectivity(I))

print('Assortativity: ', assrt.degree_assortativity_coefficient(I))

print('Local efficiency', eff.local_efficiency(I))

print('Global efficiency', eff.global_efficiency(I))

print('Density: {0:.10f}'.format(fn.density(I)))

print('Global reachness centrality:', ctr.global_reaching_centrality(I))

