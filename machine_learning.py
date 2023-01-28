import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def train_model(data, target, model_type):
    # split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

    if model_type == "random_forest":
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    elif model_type == "svm":
        model = SVR()
    elif model_type == "neural_network":
        model = MLPRegressor(hidden_layer_sizes=(100,50,25), max_iter=1000, early_stopping=True, validation_fraction=0.2)
    else:
        raise ValueError("Invalid model type")

    # train the model on the training data
    model.fit(X_train, y_train)

    # make predictions on the testing data
    y_pred = model.predict(X_test)

    # calculate the mean absolute error
    mae = mean_absolute_error(y_test, y_pred)

    return model, mae

def main():
    # load the historical data
    data = pd.read_csv("historical_data.csv")

    # select the relevant columns
    data = data[["open", "high", "low", "close", "volume"]]

    # define the target column
    target = data["close"]

    # drop the target column from the data
    data = data.drop("close", axis=1)

    # train and test the models
    random_forest_model, random_forest_mae = train_model(data, target, "random_forest")
    svm_model, svm_mae = train_model(data, target, "svm")
    neural_network_model, neural_network_mae = train_model(data, target, "neural_network")

    # print the results
    print("Random Forest MAE:", random_forest_mae)
    print("SVM MAE:", svm_mae)
    print("Neural Network MAE:", neural_network_mae)

    # save the models
    import pickle
    with open("random_forest_model.pkl", "wb") as f:
        pickle.dump(random_forest_model, f)
    with open("svm_model.pkl", "wb") as f:
        pickle.dump(svm_model, f)
    with open("neural_network_model.pkl", "wb") as f:
        pickle.dump(neural_network_model, f)

if __name__ == "__main__":
    main()

