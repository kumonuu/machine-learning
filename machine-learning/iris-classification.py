import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from seaborn import heatmap

df = pd.read_csv("iris.csv")

x = df[["sepal_length","sepal_width","petal_length","petal_width"]]
y = df["species"]
species = ["setosa","versicolor","virginica"]

le = LabelEncoder()
y = le.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.7,random_state=1)

dtc = DecisionTreeClassifier()
dtc.fit(x_train,y_train)
predicted_species = dtc.predict(x_test)

print(accuracy_score(y_test,predicted_species))
heatmap(confusion_matrix(y_test,predicted_species),annot=True,xticklabels=species,yticklabels=species)
plt.show()