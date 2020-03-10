import networkx as nx
from networkx.classes import function as fn
from networkx.algorithms import approximation as appr
from networkx.algorithms import assortativity as assrt
from networkx.algorithms import efficiency_measures as eff
from networkx.algorithms import components as comp
from networkx.algorithms import centrality as ctr

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rdm

conn_df = pd.read_csv(
    'traffic/res/ISCX_Botnet-Training.csv', 
    header = None,
    error_bad_lines = False,
    names = ['source', 'target']
)

N = nx.convert_matrix.from_pandas_edgelist(conn_df.sample(frac=0.25))
N.name = 'ISCX Botnet'

nx.draw(N, label = 'ISCX Botnet 2014, 25%', with_labels = False, font_size = 5, node_size = 0.5)
plt.title(N.name)
#fig = plt.figure()
#ax = fig.add_subplot(111)

#h = list(assrt.average_neighbor_degree(N).values())

#print(h[:10])

#ax.set_title('Grado promedio de vecinos')
#ax.set_yscale('log')
#ax.set_xlim((-0.1, 0.8))
#ax.set_xlabel('Grado promedio')
#ax.set_ylabel('Frecuencia')
#ax.hist(h, bins=np.arange(min(h), max(h) + 100, 100))
plt.show()

#print(fn.info(N))

#print('Connected components: ', comp.number_connected_components(N))

#print('Clustering coefficient: {0:.4f}'.format(
#    appr.clustering_coefficient.average_clustering(N)
#    )
#)

#print('Connectivity: ', appr.node_connectivity(N))

#print('Assortativity: ', assrt.degree_assortativity_coefficient(N))

#print('Avg nei degree: ', assrt.average_neighbor_degree(N))

#print('Local efficiency', eff.local_efficiency(N))

#print('Global efficiency', eff.global_efficiency(N))

#print('Density: {0:.10f}'.format(fn.density(N)))

