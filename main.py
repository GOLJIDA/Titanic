import pandas as pd

df = pd.read_csv('data/train.csv')

def clear_names(name):
    if '(' in name:
        name = name.split('(')
        name = name[1].split(' ')
        return name[0]
    elif 'Miss.':
        name = name.split('Miss.')
        return name[0]
    else:
        name = name.split('Mrs.')
        return name[0]


females_names = df[df.Sex=='female'][df.Survived==0]['Name']
females_names['Name'] = df[df.Sex=='female'][df.Survived==0]['Name'].apply(clear_names)


print(females_names['Sex'].mode())

# print(males_names)
# print(women_names)

