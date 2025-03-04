import pandas as pd

a = pd.read_table("./a.txt", skiprows=2)

a.to_csv("./b2.txt", index=False, header=False, quoting=3)
