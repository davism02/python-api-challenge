#Vactionpy

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import os
import json
import time
import seaborn as sns
import gmaps

from config import g_key
weather_df = pd.read_csv("../output_data/cities.csv")
weather_df
