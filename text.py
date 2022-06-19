# importing pandas as pd
import pandas as pd
# Creating the dataframe
df = pd.DataFrame(
{"A":[1, 5, 3, 4, 2],
"B":[3, 2, 4, 3, 4],
"C":[2, 2, 7, 3, 4],
 "D":[4, 3, 6, 12, 7]})
# using quantile() function to
# find the quantiles over the index axis
df.quantile([.1, .25, .5, .75], axis = 0)