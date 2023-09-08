import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import seaborn as sb

def view_word_frequency(word_counts, colormap:str, title: str, kind: str='barh', limit: int=6):
    """
    plots either a horizontal bar graph to display frequency of words top 'limit' 
    words e.g. top 20 or a pie chart to display the percentages of the top 'limit' 
    words e.g. top 20, specified by the argument kind which can be either
    strings barh or pie

    args: 
        word_counts - 
        colormap - 
        title - 
        kind - 
        limit - 
    """

    # get either last few words or first feww words
    data = word_counts[:limit].sort_values(ascending=True)
    cmap = cm.get_cmap(colormap)
    fig = plt.figure(figsize=(15, 10))
    axis = fig.subplots()
    
    if kind == 'barh':        
        axis.barh(data.index, data.values, color=cmap(np.linspace(0, 1, len(data))))

        # axis = word_counts[:limit].sort_values(ascending=True).plot(kind='barh', colormap='viridis')

        axis.set_xlabel('frequency')
        axis.set_ylabel('words')
        axis.set_title(title)
        plt.savefig(f'./figures & images/{title}.png')

        plt.show()
    elif kind == 'pie':
        axis.pie(data, labels=data.index, autopct='%.2f%%', colors=cmap(np.linspace(0, 1, len(data))))
        axis.axis('equal')
        axis.set_title(title)
        plt.savefig(f'./figures & images/{title}.png')
        plt.show()


def view_all_df_rows(df):
    pass