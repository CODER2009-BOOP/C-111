import plotly.figure_factory as ff
import pandas as pd
import csv
import random
import statistics
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data], ['Math_score'], show_hist=False)
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of population:", mean)
print("standard deviation",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
#std_deviation = statistics.std
mean = statistics.mean(mean_list)
print("mean of sampling distribution", mean)

#fig = ff.create_distplot([mean_list], ['studentMarks'], show_hist=False)
fig.add_trace(go.scatter(x = [mean,mean], y = [0,0.28], mode = 'Lines', name = "MEAN" ))
fig.show()