import pandas as pd



def category_func(category_name):
  df = pd.read_csv('emojis.csv')

  if df[df['Category'] == category_name].empty:
    print('нет такой категории')
  else:
    print(len(df.loc[df['Category'] == category_name])*100/len(df['Category']),'%')

category_func('Smileys & Emotion')
category_func('People & Body')