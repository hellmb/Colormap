from matplotlib.colors import LinearSegmentedColormap

def DefineColormap(name):
    """
    Custom colormaps

    Parameters:
    ----------
    name - string
        Name of colormap
    """

    if name == 'afternoon':
        cmap = LinearSegmentedColormap.from_list("", ["#660000","#8C0004","#C8000A","#E8A735","#E2C499"])
    elif name == 'timeless':
        cmap = LinearSegmentedColormap.from_list("", ["#16253D","#002C54","#CD7213","#EFB509"])
    elif name == 'subnautic':
        cmap = LinearSegmentedColormap.from_list("", ["#263238","#004D40","#0097A7","#F57F17", "#F9A825"])
    elif name == 'arctic':
        cmap = LinearSegmentedColormap.from_list("", ["#006C84","#6EB5C0","#E2E8E4","#FFCCBB"])
    elif name == 'sunkissed':
        cmap = LinearSegmentedColormap.from_list("", ["#D24136","#EB8A3E","#EBB582","#785A46"])
    elif name == 'berry':
        cmap = LinearSegmentedColormap.from_list("", ["#1E1F26","#283655","#4D648D","#D0E1F9"])
    elif name == 'calm':
        cmap = LinearSegmentedColormap.from_list("", ["#363237","#2D4262","#73605B","#D09683"])
    elif name == 'sea':
        cmap = LinearSegmentedColormap.from_list("", ["#021C1E","#004445","#2C7873","#6FB98F"])
    elif name == 'skittles':
        cmap = LinearSegmentedColormap.from_list("", ["#061283","#FD3C3C","#FFB74C","#138D90"])
    elif name == 'morning':
        cmap = LinearSegmentedColormap.from_list("", ["#81715E","#FAAE3D","#E38533","#E4535E"])
    elif name == 'oldtimer':
        cmap = LinearSegmentedColormap.from_list("", ["#323030","#CDBEA7","#C29545","#882426"])
    elif name == 'misty':
        cmap = LinearSegmentedColormap.from_list("", ["#04202C","#2C493F","#5B7065","#C9D1C8"])
    elif name == 'water':
        cmap = LinearSegmentedColormap.from_list("", ["#003B46","#07575B","#66A5AD","#C4DFE6"])
    elif name == 'forest':
        cmap = LinearSegmentedColormap.from_list("", ["#1B5E20", "#2E7D32", "#43A047", "#7CB342",
                                                      "#9CCC65", "#AED581", "#F1F8E9"])
    elif name == 'fall':
        cmap = LinearSegmentedColormap.from_list("", ["#78281F", "#A93226", "#C0392B", "#BA4A00",
                                                      "#DC7633", "#EDBB99", "#FBEEE6"])
    elif name == 'candy':
        cmap = LinearSegmentedColormap.from_list("", ["#AD1457","#D81B60","#FFA000","#FDD835","#FFEE58"])
    elif name == 'candy2':
        cmap = LinearSegmentedColormap.from_list("", ["#AD1457", "#D81B60", "#EC407A", "#F9A825", "#FBC02D", "#FFE082"])
    elif name == 'bubblegum':
        cmap = LinearSegmentedColormap.from_list("", ["#AD1457", "#C2185B", "#D81B60", "#EC407A",
                                                      "#F06292", "#F48FB1", "#F8BBD0"])
    elif name == 'florida':
        cmap = LinearSegmentedColormap.from_list("",["#00838F", "#FFFFFF", "#E65100"])
    elif name == 'joy':
        cmap = LinearSegmentedColormap.from_list("",["#0097A7", "#A5D6A7", "#FF8A65", "#E57373"])
    elif name == 'spring':
        cmap = LinearSegmentedColormap.from_list("",["#1E88E5", "#7CB342", "#FBC02D"])
    elif name == 'blush':
        cmap = LinearSegmentedColormap.from_list("",["#757575", "#BDBDBD", "#FFFFFF", "#FFEBEE", "#EF9A9A"])
    elif name == 'pastels':
        cmap = LinearSegmentedColormap.from_list("",["#5DADE2", "#2E86C1", "#884EA0", "#AF7AC5", "#F48FB1", "#EC407A",
                                                     "#FB8C00", "#FFB74D", "#FFE082", "#FBC02D", "#4CAF50", "#AED581"])
    elif name == 'galaxy':
        cmap = LinearSegmentedColormap.from_list("",["#1B2631", "#283747", "#633974", "#AD1457", "#F06292"])
    else:
        raise ValueError('Specify name of colormap (string) as input argument.')

    return cmap

def DiscreteColormap(name, n_colors):
    """
    Get discrete colormap 
    
    Parameters:
    ----------
    name - string
        Name of colormap
    n_colors - int
        Number of discrete colors
    """

    cmap = DefineColormap(name)._resample(n_colors)

    return cmap




