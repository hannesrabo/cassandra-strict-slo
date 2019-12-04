import re
import pandas as pd

from os import listdir
from os.path import isfile, join

def get_timestamps(filename):
    file = open(filename, "r")
    lines = list(map(lambda line: line.rstrip('\n'), file.readlines()))

    
    # Remove everything before "Starting test"
    def get_line_with_find(lines, regex):
        for index, line in enumerate(lines):
            if line.find(regex) != -1:
                return index
        return -1

    body_index = get_line_with_find(lines, 'Starting test.')

    body = lines[body_index + 1:]
    
    # Get only data lines
    regex_pattern = re.compile(
        "^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]:[0-9]{3}")
    data_lines = list(filter(regex_pattern.match, body))
    
    # Get first and last line
    first_line = data_lines[0]
    last_line = data_lines[-1]
    
    # Parse the timestamps
    start_time_string = first_line.split()[0] + ' ' + first_line.split()[1][:12]
    end_time_string = last_line.split()[0] + ' ' + last_line.split()[1][:12]

    return start_time_string, end_time_string

def get_metric_filenames(dirname):
    onlyfiles = [f for f in listdir(dirname) if isfile(join(dirname, f))]
    return onlyfiles

def create_metric_dataframe(filename, start_time_string, end_time_string):
    metrics_df = pd.read_csv(filename, parse_dates=True, infer_datetime_format=True, skipinitialspace=True)
    metrics_df = metrics_df.dropna(axis='columns', how='all')

    # Filter out rows that are before or after the benchmark
    in_benchmark = (metrics_df['Timestamp'] > start_time_string) & (metrics_df['Timestamp'] < end_time_string)
    metrics_df = metrics_df[in_benchmark]
    
    #Rename columns
    metrics_df = metrics_df.rename(columns={
        "ReadLatency1": "ReadThroughput_avg_1minute",
        "WriteLatency1": "WriteThroughput_avg_1minute"})

    # Calculate throughput
    metrics_df['ReadThroughput'] = metrics_df['ReadCount'] - metrics_df['ReadCount'].shift(1)
    metrics_df['WriteThroughput'] = metrics_df['WriteCount'] - metrics_df['WriteCount'].shift(1)

    metrics_df = metrics_df.fillna(0)

    # Remove rows with 0 throughput
    no_reads = metrics_df['ReadThroughput'] > 0
    no_writes = metrics_df['WriteThroughput'] > 0

    metrics_df = metrics_df[no_reads | no_writes]

    return metrics_df

def get_metrics(filename):
    # Get start and end time of benchmark
    start_time_string, end_time_string = get_timestamps(filename + "_stderr")

    # Get metric filenames
    metrics_dir = filename + "_metrics"
    metric_filenames = get_metric_filenames(metrics_dir)

    # Create dataframes and return them
    return map(lambda metric_filename: create_metric_dataframe(
        metrics_dir + "/" + metric_filename, start_time_string, end_time_string), metric_filenames)