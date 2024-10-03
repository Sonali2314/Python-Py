import pandas as pd
def getDataframeSize(players: pd.DataFrame) -> list[int]:
    r,c= players.shape
    l=[r,c]
    return l

players={'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df=pd.DataFrame(players)
print(f"Number of rows and columns in dataframe : {getDataframeSize(df)}")
