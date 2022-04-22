#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from random import shuffle
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# ## Deck Size can be defined here:

# In[34]:


deck = []
error = 0.167

# The range here used is the number of entries to be shuffled
for i in range(900):
    deck.append(i + 1)


# ## Functions

# In[4]:


# Function to split the deck into N/30 different parts
def cut_specs(deck):
    cut_num = int(len(deck) / 30)
    cut_len = (np.floor(len(deck) / cut_num)).astype(int)

    splits = []

    splits.append(deck[0:cut_len])
    end_len = cut_len

    for i in range(cut_num + 10):
        start_len = end_len
        end_len = end_len + cut_len

        if (len(deck) - cut_len < end_len):
            end_len = len(deck)

        splits.append(deck[start_len:end_len])

    split_lists = []
    for li in splits:
        if (li != []):
            split_lists.append(li)

    return split_lists


# In[5]:


# Function to perform the ruffle
def ruffle(sample):
    h1 = []
    h2 = []

    x = (np.floor(len(sample) / 2)).astype(int)

    for i in range(x):
        h1.append(sample[i])

    for i in range(x, len(sample)):
        h2.append(sample[i])

    len1 = 0
    len2 = 0
    ruffled = []

    while ((len(h1) > len1) and (len(h2) > len2)):
        limit1 = 1  # np.random.randint(1,2,1)[0]
        limit2 = 1  # np.random.randint(1,2,1)[0]

        end1 = len1 + limit1
        end2 = len2 + limit2

        for i in range(len1, end1):
            if (end1 < len(h1)):
                ruffled.append(h1[i])
        for i in range(len2, end2):
            if (end2 < len(h2)):
                ruffled.append(h2[i])

        if (end1 < len(h1)):
            len1 = end1

        if (end2 < len(h2)):
            len2 = end2

        if (end1 >= len(h1)):
            break

        if (end2 >= len(h2)):
            break

    if (len1 < len(h1)):
        for j in range(len1, len(h1)):
            ruffled.append(h1[j])
    if (len2 < len(h2)):
        for k in range(len2, len(h2)):
            ruffled.append(h2[k])

    return ruffled


# In[6]:


# Function to rearrange the cuts into deck using a random sequence
def results(sample):
    sequence = []

    for i in range(len(sample)):
        sequence.append(i)

    shuffle(sequence)

    result = []

    for i in range(len(sample)):
        result = result + sample[sequence[i - 1]]

    return result


# In[7]:


# Function to compile the complete process of shuffle based on the procedure
# First the deck is ruffled, then it is divided into multiple stacks and the stacks are rearranged randomly
def compile_(deck, test_num):
    deck_sub = deck
    for i in range(test_num):
        deck_inter = ruffle(deck_sub)
        test = cut_specs(deck_inter)
        result = results(test)
        deck_sub = result

    return result


# In[8]:


# Function to concatinate the shuffled deck based on how many times we want the suffling process to repeat
def concat(deck, num):
    df = pd.DataFrame()
    for i in range(num):
        result = []
        result = compile_(deck, 7)
        df[i + 1] = result

    return df

# In[9]:


# Function to get moving averages of the shuffled series
def getMeans(df):
    global deck
    x = 0
    samp = []
    for i in range(len(deck) - 1):
        samp.append(df[1][x: x + 50])
        x = x + 1
        if (x > (len(deck) - 51)):
            break

    means = []
    for i in range(len(deck) - 50):
        means.append(samp[i].mean())

    return means


# In[35]:


# Function to check for outliers in moving averages in accordance with central limit theorem
# Here we define the percentage error or limit from the center accepted in testing for central limit theorem
def outliers(means):
    global deck, error
    count = 0

    for i in range(len(deck) - 50):

        if (means[i] > (len(deck) / 2) - ((len(deck) / 2) * error)) and (
                means[i] < (len(deck) / 2) + ((len(deck) / 2) * error)):
            count = count + 1

    return count


# ### To get multiple outputs

# In[27]:


# Declaring global dataframes for getting shuffled series and means output

series_df = pd.DataFrame(deck)

means_df = pd.DataFrame(deck[0:(len(deck) - 50)])

series_num = 1


# In[29]:


# Function to add a passed series and it's moving averages into specific dataframes
def getSeriesWithMeans():
    global series_num, count, df_out, deck
    for i in range(150):
        if (count == (df_out.shape[0]) - 50):
            series_df[series_num] = df_out
            means_df[series_num] = getMeans(df_out)
            series_num = series_num + 1

            df_out = concat(deck, 1)
            means = getMeans(df_out)
            count = outliers(means)
            break
        else:
            df_out = concat(deck, 1)
            means = getMeans(df_out)
            count = outliers(means)

        # In[48]:


# Function to visualize Central Limit Theorem
# If the input value changes from 1500 and the acceptance limit can be adjusted manually in this function
def visualizeCentralLimitTheorem():
    global count, df_out, means, deck, error

    m = (len(deck) / 2)
    l = len(deck) - 50
    ya = (len(deck) / 2) - ((len(deck) / 2) * error)
    yb = (len(deck) / 2) + ((len(deck) / 2) * error)

    for i in range(150):

        if (count == ((df_out.shape[0]) - 50)):

            print("\n\t Number of iterations for optimum series = {}.".format(i + 1))

            fig = go.Figure(data=go.Scatter(x=np.arange(0, 1470, step=1), y=means))
            fig.add_shape(
                # Line Horizontal
                type="line",
                x0=-1,
                y0=yb,
                x1=l,
                y1=yb,
                line=dict(
                    color="Pink",
                    width=4,
                ))
            fig.add_shape(
                # Line Horizontal
                type="line",
                x0=-1,
                y0=ya,
                x1=l,
                y1=ya,
                line=dict(
                    color="LightSeaGreen",
                    width=4,
                ))
            fig.add_shape(
                # Line Horizontal
                type="line",
                x0=-1,
                y0=m,
                x1=l,
                y1=m,
                line=dict(
                    color="Black",
                    width=2,
                    dash="dashdot"
                ))

            fig.update_layout(
                yaxis=dict(
                    tickmode='linear',
                    tick0=600,
                    dtick=25
                )
            )

            fig.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=np.arange(0, len(deck) - 1, step=100),
                    ticktext=np.arange(1, len(deck), step=100)
                )
            )

            fig.show()

            # df_out = df.copy()

            df_out = concat(deck, 1)
            means = getMeans(df_out)
            count = outliers(means)

            break

        else:
            df_out = concat(deck, 1)
            means = getMeans(df_out)
            count = outliers(means)


# ### Dataframe to get the test output

# In[13]:


# Creating a DataFrame to store shuffled series for further test
df_out = concat(deck, 1)

# Getting moving averages
means = getMeans(df_out)

# getting the number of moving averages passing central limit theorem
count = outliers(means)

# In[32]:


# df_out.style.background_gradient(cmap = 'gist_earth_r')


# In[210]:


# Getting 15 sets of series and moving averages that pass central limit theorem
for i in range(50):
    if (series_num == 16):
        break
    else:
        getSeriesWithMeans()

# In[213]:


# Setting the correct index of obtained dataframe
series_df = series_df.set_index(0)
means_df = means_df.set_index(0)

# In[216]:


# Checking the output of series
series_df

# In[1]:


# series_df.style.background_gradient(cmap = 'gist_earth_r')


# In[215]:


# Checking the output of moving averages
means_df

# In[ ]:


# means_df.style.background_gradient(cmap = 'gist_earth_r')


# In[50]:


# To vizualize if the central limit thoerem is passed and the code is working correctly
visualizeCentralLimitTheorem()

# In[217]:


series_df.to_csv('Series_Output.csv')
means_df.to_csv('Means_Output.csv')

# In[30]:


getSeriesWithMeans()

# In[32]:


series_df

# In[ ]:
