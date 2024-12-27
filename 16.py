import pandas as pd

space_x_missions_csv = "https://raw.githubusercontent.com/BriantOliveira/SpaceX-Dataset/master/dataset/SpaceX-Missions.csv"
df = pd.read_csv(space_x_missions_csv)
launches_dataset=df[['Launch Date','Launch Time','Launch Time']]
print(launches_dataset.head())
print(df["Customer Country"])
print(pd.unique(df["Customer Country"]))
launches_by_country=df.groupby("Customer Country")
print(launches_by_country.groups)
print(df["Payload Mass"]>40000)
print(df[["Customer Country"] == "United States"]["Payload Mass"].median())