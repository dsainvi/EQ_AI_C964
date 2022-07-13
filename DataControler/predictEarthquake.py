import pandas as pd
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tkinter import Tk, Label, Button, Frame
from DataControler import datawizerd

data = datawizerd.datawiz()
# eqfour = sns.kdeplot()
# heatmap
numeric_columns = [column for column in data.columns if data.dtypes[column] != 'object']
corr = data[numeric_columns].corr()
sns.heatmap(corr, annot=True, vmin=-1.0, vmax=1.0)
# corr.to_csv("dataSet/cor.csv")

numeric_columns.remove('Status')
scaler = StandardScaler()
standardized_df = pd.DataFrame(scaler.fit_transform(data[numeric_columns].copy()), columns=numeric_columns)

# data.to_csv("dataSet/eq_database.csv")

data['Type'].unique()
def onehot_encode(df, columns, prefixes):
    df = df.copy()
    for column, prefix in zip(columns, prefixes):
        dummies = pd.get_dummies(df[column], prefix=prefix)
        df = pd.concat([df, dummies], axis=1)
        df = df.drop(column, axis=1)
    return df


data = onehot_encode(
    data, ['Type', 'Magnitude Type', 'Source', 'Location Source', 'Magnitude Source'],  ['t', 'mt', 's', 'ls', 'ms']
)

# plot 4

# strip and split

# model training
y = data.loc[:, 'Status']
X = data.drop('Status', axis=1)
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=56)
print(X.shape)
y.mean()
inputs = tf.keras.Input(shape=(105,))
x = tf.keras.layers.Dense(64, activation='relu')(inputs)
x = tf.keras.layers.Dense(64, activation='relu')(x)
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(inputs, outputs)
model.compile(
    optimizer='adam',loss='binary_crossentropy', metrics=[tf.keras.metrics.AUC(name='auc')]
)
batch_size = 33
epochs = 31
history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    batch_size=batch_size,
    epochs=epochs,
    callbacks=[tf.keras.callbacks.ReduceLROnPlateau()],
    verbose=0
)
epochs_range = range(epochs)
train_loss, val_loss = history.history['loss'], history.history['val_loss']
train_auc, val_auc = history.history['auc'], history.history['val_auc']

# model.evaluate(X_test, y_test)
# len(y_test)


