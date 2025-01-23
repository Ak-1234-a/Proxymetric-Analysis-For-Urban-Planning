from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_model(features, labels):
    """
    Train a machine learning model using logistic regression to classify connectivity.
    """
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    
    # Initialize and train logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Make predictions and calculate accuracy
    y_pred = model.predict(X_test)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    
    return model

def predict(model, features):
    """
    Predict connectivity for a new location based on its features.
    """
    return model.predict([features])
