"""


Examples used in talks

"""


def example_networkx(ax=None, **options):
    """
    
        example using networks
        
        :param      ax:          axis
        :param      options:     look at the code
        :return:                 ax
        
    """
    import networkx as nx
    import matplotlib.pyplot as plt

    G=nx.random_geometric_graph(200,0.125)
    # position is stored as node attribute data for random_geometric_graph
    pos=nx.get_node_attributes(G,'pos')

    # find node near center (0.5,0.5)
    dmin=1
    ncenter=0
    for n in pos:
        x,y=pos[n]
        d=(x-0.5)**2+(y-0.5)**2
        if d<dmin:
            ncenter=n
            dmin=d

    # color by path length from node near center
    p=nx.single_source_shortest_path_length(G,ncenter)

    if ax is None:
        _, ax = plt.subplots(nrows=1, ncols=1, figsize=options.get('figsize', (5,5)))
                
    nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4, ax=ax)
    nx.draw_networkx_nodes(G,pos,nodelist=p.keys(),
                           node_size=80, ax=ax)

    ax.set_xlim(-0.05,1.05)
    ax.set_ylim(-0.05,1.05)
    ax.axis('off')    
    return ax
