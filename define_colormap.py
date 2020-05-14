from matplotlib.colors import LinearSegmentedColormap

def DefineColormap(n):
    """
    function for deciding custom colormaps
    param n: name of colormap, string
    """

    if n == 'afternoon':
        colormap = LinearSegmentedColormap.from_list("", ["#8C0004","#C8000A","#E8A735","#E2C499"])
    elif n == 'timeless':
        colormap = LinearSegmentedColormap.from_list("", ["#16253D","#002C54","#CD7213","#EFB509"])
    elif n == 'arctic':
        colormap = LinearSegmentedColormap.from_list("", ["#006C84","#6EB5C0","#E2E8E4","#FFCCBB"])
    elif n == 'sunkissed':
        colormap = LinearSegmentedColormap.from_list("", ["#D24136","#EB8A3E","#EBB582","#785A46"])
    elif n == 'berry':
        colormap = LinearSegmentedColormap.from_list("", ["#1E1F26","#283655","#4D648D","#D0E1F9"])
    elif n == 'calm':
        colormap = LinearSegmentedColormap.from_list("", ["#363237","#2D4262","#73605B","#D09683"])
    elif n == 'sea':
        colormap = LinearSegmentedColormap.from_list("", ["#021C1E","#004445","#2C7873","#6FB98F"])
    elif n == 'skittles':
        colormap = LinearSegmentedColormap.from_list("", ["#061283","#FD3C3C","#FFB74C","#138D90"])
    elif n == 'morning':
        colormap = LinearSegmentedColormap.from_list("", ["#81715E","#FAAE3D","#E38533","#E4535E"])
    elif n == 'oldtimer':
        colormap = LinearSegmentedColormap.from_list("", ["#323030","#CDBEA7","#C29545","#882426"])
    elif n == 'misty':
        colormap = LinearSegmentedColormap.from_list("", ["#04202C","#2C493F","#5B7065","#C9D1C8"])
    elif n == 'water':
        colormap = LinearSegmentedColormap.from_list("", ["#003B46","#07575B","#66A5AD","#C4DFE6"])
    elif n == 'forest':
        colormap = LinearSegmentedColormap.from_list("", ["#1B5E20", "#2E7D32", "#43A047", "#7CB342", "#9CCC65", "#AED581", "#F1F8E9"])
    elif n == 'fall':
        colormap = LinearSegmentedColormap.from_list("", ["#78281F", "#A93226", "#C0392B", "#BA4A00", "#DC7633", "#EDBB99", "#FBEEE6"])
    elif n == 'candy':
        colormap = LinearSegmentedColormap.from_list("", ["#AD1457","#D81B60","#FFA000","#FDD835","#FFEE58"])
    elif n == 'candy2':
        colormap = LinearSegmentedColormap.from_list("", ["#AD1457", "#D81B60", "#EC407A", "#F9A825", "#FBC02D", "#FFE082"])
    elif n == 'bubblegum':
        colormap = LinearSegmentedColormap.from_list("", ["#AD1457", "#C2185B", "#D81B60", "#EC407A", "#F06292", "#F48FB1", "#F8BBD0"])
    else:
        raise ValueError('Specify name of colormap (string) as input argument.')

    return colormap
