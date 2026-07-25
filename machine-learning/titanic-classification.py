import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from seaborn import heatmap

df = pd.read_csv("titanic.csv")
df = df.drop(columns="Cabin")

# preprocessing
le = LabelEncoder()
df["Embarked"] = le.fit_transform(df["Embarked"])
df["Sex"] = le.fit_transform(df["Sex"])
df["Age"] = df["Age"].fillna(value=df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(value=df["Embarked"].median())

x = df[["Pclass","Age","Sex","Fare","Embarked"]]
y = df["Survived"]
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8,random_state=42)

dtc = DecisionTreeClassifier()
dtc.fit(x_train,y_train)
y_pred = dtc.predict(x_test)

print(df["Survived"].value_counts())
print(accuracy_score(y_test,y_pred))
heatmap(confusion_matrix(y_test,y_pred),annot=True)

plt.show()