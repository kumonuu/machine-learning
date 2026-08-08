import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from seaborn import heatmap

df = pd.read_csv("winequality-red.csv")
print(df.info())

x = df.drop(columns="quality")
y = df["quality"]

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8,random_state=30)

dtc = DecisionTreeClassifier()
dtc.fit(x_train,y_train)
y_pred = dtc.predict(x_test)

print(accuracy_score(y_test,y_pred))
print(y.value_counts())
heatmap(confusion_matrix(y_test,y_pred),annot=True)

plt.show()
