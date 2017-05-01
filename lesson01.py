import pandas as pd

def test_run():
    df=pd.read_csv("/Users/huixueshao/Downloads/table.csv")
    print(df[10:21])

if __name__=="__main__":
    test_run()

#print(__name__)
#print(__doc__))