import pandas as pd

def main():
    df = pd.read_csv('gender2.csv', encoding ="ANSI")
    newdf = df.iloc[:,[0,1,6,11]]
    newdf = newdf.rename(columns= {'2022년_계_총인구수' : 'Total', '2022년_남_총인구수' : 'Male',  '2022년_여_총인구수' : 'Female'})
    
    print(newdf)
    
if __name__ == '__main__':
    main()
