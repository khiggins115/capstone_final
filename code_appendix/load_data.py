import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



# load in the health data. Accepts a string that says what kind of data is desired, 
# and uses and if/elif statement to load the corresponding dataset
def load_mortality():
    df = pd.read_csv('../data/cleaned/self_harm_mortality_1980_2014.csv', dtype={'FIPS': object})
    return df

# loads cleaned alcohol use data
def alcohol_use(use_type):
    if use_type == 'Any': 
        df = pd.read_csv('../data/cleaned/alcohol_use_any_2002_2012.csv', dtype={'FIPS': 'object'})
    elif use_type == 'Heavy':
        df = pd.read_csv('../data/cleaned/alcohol_use_heavy_prop_heavy_2005_2012.zip', dtype={'FIPS': 'object'})
    elif use_type == 'Binge':
        df = pd.read_csv('../data/cleaned/alcohol_use_binge_prop_binge_2002_2012.zip', dtype={'FIPS': 'object'})

    return df

# load unemployment
def load_mortality():
    df = pd.read_csv('../data/cleaned/unemployment_1990_2019.csv', dtype={'FIPS': object})
    return df


# load alcohol_use, 
def self_harm_alcohol(use_type):
    if use_type == 'Any': 
        df = pd.read_csv('../data/cleaned/selfharm_alcohol_joins/selfharm_join_alcohol_any.csv', dtype={'FIPS': 'object'})
    elif use_type == 'Heavy':
        df = pd.read_csv('../data/cleaned/selfharm_alcohol_joins/selfharm_join_heavy_prop_heavy.csv', dtype={'FIPS': 'object'})
    elif use_type == 'Binge':
        df = pd.read_csv('../data/cleaned/selfharm_alcohol_joins/selfharm_join_binge_prop_binge.csv', dtype={'FIPS': 'object'})
    
    df.dropna(inplace=True)

    return df


