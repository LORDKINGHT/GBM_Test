# pip install pandas
# pip install -U scikit-learn
# pip install keras

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

data = pd.read_excel("data_customer_classification.xlsx")

customer_data = data.groupby('customer_id').agg({
    'trans_date': 'count',
    'tran_amount': ['mean', 'max']
}).reset_index()

customer_data.columns = ['customer_id', 'frequency', 'avg_spend', 'max_spend']

label_encoder = LabelEncoder()
customer_data['category'] = label_encoder.fit_transform(pd.qcut(customer_data['max_spend'], q=3, labels=['low', 'medium', 'high']))

X = customer_data.drop(['customer_id', 'category'], axis=1)
y = customer_data['category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

y_train_categorical = to_categorical(y_train)
y_test_categorical = to_categorical(y_test)

model = Sequential()
model.add(Dense(32, input_dim=X_train_scaled.shape[1], activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train_scaled, y_train_categorical, epochs=10, batch_size=32, verbose=1)

loss, accuracy = model.evaluate(X_test_scaled, y_test_categorical)
print("Accuracy ", accuracy)