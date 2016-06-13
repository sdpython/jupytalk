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

    G = nx.random_geometric_graph(200, 0.125)
    # position is stored as node attribute data for random_geometric_graph
    pos = nx.get_node_attributes(G, 'pos')

    # find node near center (0.5,0.5)
    dmin = 1
    ncenter = 0
    for n in pos:
        x, y = pos[n]
        d = (x - 0.5) ** 2 + (y - 0.5) ** 2
        if d < dmin:
            ncenter = n
            dmin = d

    # color by path length from node near center
    p = nx.single_source_shortest_path_length(G, ncenter)

    if ax is None:
        _, ax = plt.subplots(
            nrows=1, ncols=1, figsize=options.get('figsize', (5, 5)))

    nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=p.keys(),
                           node_size=80, ax=ax)

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.axis('off')
    return ax


def example_confidence_interval(ax=None, seaborn=False, **options):
    """
    
        draw pseudo confidence interval for a regression in a matplotlib
    
        :param      ax:          axis
        :param      seaborn:     uses *seaborn* instead of *matplotlib*
        :param      options:     look at the code
        :return:                 ax
        
    """
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots(
            nrows=1, ncols=1, figsize=options.get('figsize', (5, 5)))

    import scipy
    import numpy
    nx, nboot = 22, 400
    x = scipy.linspace(0.0, 1.0, nx)
    data = x + numpy.random.normal(loc=0.0, scale=0.1, size=nx)
    yp = scipy.polyfit(x, data, 1)
    y = scipy.polyval(yp, x)

    if seaborn:
        from seaborn import regplot
        return regplot(x, data, ax=ax)
    else:
        r = data - y
        for i in range(nboot):
            pc = scipy.polyfit(
                x, y + r[scipy.random.randint(0, nx - 1, nx)], 1)
            ax.plot(x, scipy.polyval(pc, x), 'k-',
                    linewidth=2, alpha=3.0 / float(nboot))
        ax.plot(x, y, 'k-')
        ax.plot(x, data, 'ko')
        return ax


def example_basemap(ax=None, **options):
    """
    
        draw a map of France
    
        :param      ax:          axis
        :param      options:     look at the code
        :return:                 ax
        
    """
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots(
            nrows=1, ncols=1, figsize=options.get('figsize', (5, 5)))

    from mpl_toolkits.basemap import Basemap
    import numpy
    m = Basemap(llcrnrlon=-5, llcrnrlat=40, urcrnrlon=20, urcrnrlat=56,
                resolution='i', projection='cass', lon_0=2.34, lat_0=48,
                ax=ax)
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='lightgrey', lake_color='#AAAAFF')
    m.drawparallels(numpy.arange(-40, 61., 2.))
    m.drawmeridians(numpy.arange(-20., 21., 2.))
    m.drawmapboundary(fill_color='#BBBBFF')
    return ax
