import pandas as pd
penguins = pd.read_csv('penguins_cleaned.csv')

#encoding sex, species and island
df = penguins.copy()
target ='species'   #gols is to predict the species
encode = ['sex','island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

X = df.drop('species', axis=1)
Y = df['species']

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X, Y)

import pickle
pickle.dump(clf, open('penguins_clf.pkl', 'wb'))