from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, root_mean_squared_error
import os
from ml.utils import model_trainer, save_model_
from utils import SEED

@model_trainer
def train_random_forest(X_train, X_test, y_train, y_test, save_model=False):
    model = RandomForestRegressor(n_estimators=100, max_depth=20, random_state=SEED, n_jobs=-1)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    rmse = root_mean_squared_error(y_test, y_pred)
    print(f'RMSE: {rmse:.4f}')
    r2 = r2_score(y_test, y_pred)
    print(f'r2: {r2:.4f}')

    if save_model:
        if not os.path.exists("./saved_model"):
            os.mkdir("./saved_model")
        save_model_(model, './saved_model/random_forest.pkl')

    return model
