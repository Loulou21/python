import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Ce jeu de données contient les logs de capteurs de smartphone sur une trentaine d'individus en train d'effectuer 
# des activités (s'assoir, se mettre debout, marcher, etc). 
# L'objectif sera de prédire à partir des logs de capteurs le type d'activités que le sujet est en train d'effectuer.

train = pd.read_csv("/Users/louisadam/Downloads/archive/train.csv")
test  = pd.read_csv("/Users/louisadam/Downloads/archive/test.csv")

X_train = train[train.columns[:-2]]
y_train = train['Activity']

X_test = test[test.columns[:-2]]
y_test = test['Activity']

print(train.shape)

rfc = RandomForestClassifier(n_estimators=50, oob_score=True)

model = rfc.fit(X_train, y_train) #création random forest à partir du jeu d'essai train

pred = rfc.predict(X_test)
print("accuracy {:.2f}".format(accuracy_score(y_test, pred)))