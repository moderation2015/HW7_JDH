import pandas as pd

def main():
    df = pd.DataFrame({'unit price': [1000, 280, 900], 'number': [25, 120, 30]}, index=['store1', 'store2','store3'])
    print(df)

    df['total price'] = df['unit price'] * df['number']
    print(df)

    df2 = df.sort_values(by ='total price' ,ascending = False)
    print(df2.head(2))
    
if __name__ == '__main__':
    main()
