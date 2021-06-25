import pandas as pd

heatmap = pd.read_csv("recombination_heatmap.csv",index_col="label")
print(heatmap)
heatmap.eq(1).sum(axis=1).to_csv("isolate_import_num.csv")