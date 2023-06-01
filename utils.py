import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.ticker as ticker
import seaborn as sns
import os


def sample_difference(x, t):
    '''Returns the absolute difference between a sample and a fixed target value.'''
    return np.abs(x - t) 

def target_deviation(X, N, t):
    '''Returns the standard deviation of N samples from a fixed target value.'''
    return np.sqrt(np.sum(sample_difference(X, t)**2) / (N - 1))

def weekly_split(df):
    df_1 = df.loc['2023-05-01':'2023-05-07']
    df_2 = df.loc['2023-05-08':'2023-05-14']
    df_3 = df.loc['2023-05-15':'2023-05-21']
    df_4 = df.loc['2023-05-22':'2023-05-28']
    return df_1, df_2, df_3, df_4

def plot_weekly_target_deviation(x, y, threshold=1.0):
    sns.barplot(x=x, y=y)
    plt.axhline(y=threshold, color='r', linestyle='--')
    plt.title('Target Deviation of Strength Measurements [MPa]')
    plt.show()

def set_daily_xticks_dictionary(df):
    '''Returns a dictionary of xticks for each day in a dataframe in the form 
    {'yyy-mm-dd': 'Mon', ...}.'''
    xticks_dict = {}
    for i in range(len(df)):
        xticks_dict[df.index[i].strftime('%Y-%m-%d')] = df.index[i].strftime('%a')
    return xticks_dict

def plot_daily_fineness_ratio(df_1, df_2, df_3, df_4):
    # plotting the fineness ratio over time, with 4 subplots for each week of data and a threshold line of 1.0 and using the clinker phase as the marker color

    # creating a color values list for the clinker phase
    color_values1 = df_1['C3S clinker phase [%]']
    color_values2 = df_2['C3S clinker phase [%]']
    color_values3 = df_3['C3S clinker phase [%]']
    color_values4 = df_4['C3S clinker phase [%]']

    # creating a colormap for the clinker phase
    cmap = plt.cm.get_cmap('viridis')

    # Set the minimum and maximum values for the colorbars
    #vmin1 = color_values1.min()
    #vmax1 = color_values1.max()

    #vmin2 = color_values2.min()
    #vmax2 = color_values2.max()

    #vmin3 = color_values3.min()
    #vmax3 = color_values3.max()

    #vmin4 = color_values4.min()
    #vmax4 = color_values4.max()

    # Create a normalization object
    #norm1 = colors.Normalize(vmin=vmin1, vmax=vmax1)
    #norm2 = colors.Normalize(vmin=vmin2, vmax=vmax2)
    #norm3 = colors.Normalize(vmin=vmin3, vmax=vmax3)
    #norm4 = colors.Normalize(vmin=vmin4, vmax=vmax4)

    # creating a dictionary of xticks for each day in the dataframe
    xticks_dict1 = set_daily_xticks_dictionary(df_1)
    xticks_dict2 = set_daily_xticks_dictionary(df_2)
    xticks_dict3 = set_daily_xticks_dictionary(df_3)
    xticks_dict4 = set_daily_xticks_dictionary(df_4)

    fig, axes = plt.subplots(2, 2, figsize=(13, 13), sharex=False, sharey=True) 

    axes[0, 0].scatter(df_1.index, df_1['fineness ratio'], marker='o', c=color_values1, cmap=cmap)
    axes[0, 0].axhline(y=1.0, color='r', linestyle='--')
    axes[0, 0].set_title('Week 1')
    axes[0, 0].set_xticklabels(xticks_dict1.values(), rotation=45)
    # adding a colorbar
    plt.colorbar(plt.cm.ScalarMappable(cmap=cmap), ax=axes[0, 0], label='Normalized C3S phase')

    axes[0, 1].scatter(df_2.index, df_2['fineness ratio'], marker='o', c=color_values2, cmap=cmap)
    axes[0, 1].axhline(y=1.0, color='r', linestyle='--')
    axes[0, 1].set_title('Week 2')
    axes[0, 1].set_xticklabels(xticks_dict2.values(), rotation=45)
    # adding a colorbar
    plt.colorbar(plt.cm.ScalarMappable(cmap=cmap), ax=axes[0, 1], label='Normalized C3S phase')

    axes[1, 0].scatter(df_3.index, df_3['fineness ratio'], marker='o', c=color_values3, cmap=cmap)
    axes[1, 0].axhline(y=1.0, color='r', linestyle='--')
    axes[1, 0].set_title('Week 3')
    axes[1, 0].set_xticklabels(xticks_dict3.values(), rotation=45)
    # adding a colorbar
    plt.colorbar(plt.cm.ScalarMappable(cmap=cmap), ax=axes[1, 0], label='Normalized C3S phase')

    axes[1, 1].scatter(df_4.index, df_4['fineness ratio'], marker='o', c=color_values4, cmap=cmap)
    axes[1, 1].axhline(y=1.0, color='r', linestyle='--')
    axes[1, 1].set_title('Week 4')
    axes[1, 1].set_xticklabels(xticks_dict4.values(), rotation=45)
    # adding a colorbar
    plt.colorbar(plt.cm.ScalarMappable(cmap=cmap), ax=axes[1, 1], label='Normalized C3S phase')

    plt.suptitle('Fineness Ratio Over Time')
    plt.show()