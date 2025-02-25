from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.metrics import r2_score, root_mean_squared_error
import os
from ml.utils import model_trainer, min_max_scale, save_model_

@model_trainer
def train_linear_regression(X_train, X_test, y_train, y_test, save_model=False):
    # X_train, X_test, y_train, y_test = min_max_scale(X_train, X_test, y_train, y_test)
    model = LinearRegression(n_jobs=-1)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    rmse = root_mean_squared_error(y_test, y_pred)
    print(f'RMSE: {rmse:.4f}')
    r2 = r2_score(y_test, y_pred)
    print(f'r2: {r2:.4f}')

    if save_model:
        if not os.path.exists("./saved_model"):
            os.mkdir("./saved_model")
        save_model_(model, './saved_model/linear_regression.pkl')

    return model


@model_trainer
def train_elasticnet_regression(X_train, X_test, y_train, y_test, save_model=False):
    # X_train, X_test, y_train, y_test = min_max_scale(X_train, X_test, y_train, y_test)
    model = ElasticNet(alpha=0.1, l1_ratio=0.5)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    
    rmse = root_mean_squared_error(y_test, y_pred)
    print(f'RMSE: {rmse:.4f}')
    r2 = r2_score(y_test, y_pred)
    print(f'r2: {r2:.4f}')

    if save_model:
        if not os.path.exists("./saved_model"):
            os.mkdir("./saved_model")
        save_model_(model, './saved_model/elasticnet_regression.pkl')

    return model