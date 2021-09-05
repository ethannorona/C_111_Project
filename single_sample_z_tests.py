import csv
import random
import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("population mean:- ",population_mean)

def random_set_of_means(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["Reading Time"], show_hist = False)
    fig.show()

def setup():   
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)
    print("sample mean:- ",mean)
    print("sample standard deviation:- ",std_deviation)
    
    first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
    second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
    third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)
    print("std1:- ", first_std_deviation_start, first_std_deviation_end)
    print("std2:- ", second_std_deviation_start, second_std_deviation_end)
    print("std3:- ", third_std_deviation_start, third_std_deviation_end)
    
    df = pd.read_csv("data.csv")
    data = df["reading_time"].tolist()
    mean_of_sample_1 = statistics.mean(data)
    print("mean of sample 1:- ", mean_of_sample_1)
    
    z_score = (mean_of_sample_1 - mean)/std_deviation
    print("z score:- ",z_score)
    
    fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.4], mode="lines", name="MEAN"))
    fig.add_trace(go.Scatter(x=[mean_of_sample_1,mean_of_sample_1], y=[0,0.4], mode="lines", name="MEAN OF SAMPLE 1"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start], y=[0,0.4], mode="lines", name="STANDARD DEVIATION 1 START"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end], y=[0,0.4], mode="lines", name="STANDARD DEVIATION 1 END"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start], y=[0,0.4], mode="lines", name="STANDARD DEVIATION 2 START"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end], y=[0,0.4], mode="lines", name="STANDARD DEVIATION 2 END"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.4], mode="lines", name="STANDARD DEVIATION 3 START"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.4], mode="lines", name="STANDARD DEVIATION 3 END"))
    fig.show()
setup()    
