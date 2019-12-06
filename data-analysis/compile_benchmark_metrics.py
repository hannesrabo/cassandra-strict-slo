from statistics import mean
import numpy as np

def get_read_median(dataframe):
    return dataframe['ReadThroughput'].median()

def get_write_median(dataframe):
    return dataframe['WriteThroughput'].median()

def get_statistics(dataframe_list):
    read_medians = list(map(get_read_median, dataframe_list))
    write_medians = list(map(get_write_median, dataframe_list))
    
    read_compiled_mean = mean(read_medians)
    read_compiled_variance = np.var(read_medians)
    write_compiled_mean = mean(write_medians)
    write_compiled_variance = np.var(write_medians)
    
    return read_compiled_mean, read_compiled_variance, write_compiled_mean, write_compiled_variance