import os
import matplotlib.pyplot as plt
from xgboost import XGBRegressor, plot_importance
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.inspection import PartialDependenceDisplay
from ml.utils import model_trainer, save_model_
from utils import ROOMINFO_COLUMNS, TYPEINFO_COLUMNS, AREAINFO_COLUMNS, AROUNDINFO_COLUMNS, BASEINFO_COLUMNS, TRANSACTION_COLUMNS, MACROINFO_COLUMNS


def plot_summary(model, X_train):
    plt.figure(figsize=(10, 8))
    importance_type = 'weight'
    max_num_features = 10
    plot_importance(model, importance_type=importance_type, max_num_features=max_num_features)
    plt.title(f'Top {max_num_features} Feature Importances by {importance_type}')
    plt.yticks(rotation=45)
    if not os.path.exists('./output'):
        os.mkdir('./output')
    if not os.path.exists('./output/boosting'):
        os.mkdir('./output/boosting')
    plt.savefig("./output/boosting/importance.png")
    print("Save figure ./output/boosting/importance.png")

    y_max = 5000
    selected_features = ROOMINFO_COLUMNS
    plt.figure(figsize=(15, 10))
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_ylim(0, y_max)
    PartialDependenceDisplay.from_estimator(
        model, X_train, features=selected_features, 
        feature_names=X_train.columns, grid_resolution=50, ax=ax, kind='average'
    )
    ax.set_title('Partial Dependence Plots for Top roomInfo Features', fontsize=16)
    plt.tight_layout() 
    plt.savefig('./output/boosting/partial_dependence_roomInfo.png')
    print("Save figure ./output/boosting/partial_dependence_roomInfo.png")

    selected_features = TYPEINFO_COLUMNS
    plt.figure(figsize=(15, 10))
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_ylim(0, y_max)
    PartialDependenceDisplay.from_estimator(
        model, X_train, features=selected_features, 
        feature_names=X_train.columns, grid_resolution=50, ax=ax, kind='average'
    )
    ax.set_title('Partial Dependence Plots for typeInfo Features', fontsize=16)
    plt.tight_layout() 
    plt.savefig('./output/boosting/partial_dependence_typeInfo.png')
    print("Save figure ./output/boosting/partial_dependence_typeInfo.png")

    selected_features = AREAINFO_COLUMNS
    plt.figure(figsize=(15, 10))
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_ylim(0, y_max)
    PartialDependenceDisplay.from_estimator(
        model, X_train, features=selected_features, 
        feature_names=X_train.columns, grid_resolution=50, ax=ax, kind='average'
    )
    ax.set_title('Partial Dependence Plots for areaInfo Features', fontsize=16)
    plt.tight_layout() 
    plt.savefig('./output/boosting/partial_dependence_areaInfo.png')
    print("Save figure ./output/boosting/partial_dependence_areaInfo.png")

    filtered_data = X_train[(X_train['lng'] != -1) & (X_train['lat'] != -1)]
    selected_features = AROUNDINFO_COLUMNS
    plt.figure(figsize=(15, 10))
    fig, ax = plt.subplots(figsize=(15, 10))
    PartialDependenceDisplay.from_estimator(
        model, filtered_data, features=selected_features, 
        feature_names=filtered_data.columns, grid_resolution=50, ax=ax, kind='average'
    )
    ax.set_title('Partial Dependence Plots for aroundInfo Features', fontsize=16)
    plt.tight_layout()
    plt.savefig('./output/boosting/partial_dependence_aroundInfo.png')
    print("Save figure ./output/boosting/partial_dependence_aroundInfo.png")
    
    selected_features = BASEINFO_COLUMNS
    plt.figure(figsize=(15, 10))
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_ylim(0, y_max)
    PartialDependenceDisplay.from_estimator(
        model, X_train, features=selected_features, 
        feature_names=X_train.columns, grid_resolution=50, ax=ax, kind='average'
    )
    ax.set_title('Partial Dependence Plots for baseInfo Features', fontsize=16)
    plt.tight_layout() 
    plt.savefig('./output/boosting/partial_dependence_baseInfo.png')
    print("Save figure ./output/boosting/partial_dependence_baseInfo.png")

    selected_features = TRANSACTION_COLUMNS
    plt.figure(figsize=(15, 10))
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_ylim(0, y_max)
    PartialDependenceDisplay.from_estimator(
        model, X_train, features=selected_features, 
        feature_names=X_train.columns, grid_resolution=50, ax=ax, kind='average'
    )
    ax.set_title('Partial Dependence Plots for transaction Features', fontsize=16)
    plt.tight_layout() 
    plt.savefig('./output/boosting/partial_dependence_transaction.png')
    print("Save figure ./output/boosting/partial_dependence_transaction.png")

    selected_features = MACROINFO_COLUMNS
    plt.figure(figsize=(15, 10))
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_ylim(0, y_max)
    PartialDependenceDisplay.from_estimator(
        model, X_train, features=selected_features, 
        feature_names=X_train.columns, grid_resolution=50, ax=ax, kind='average'
    )
    ax.set_title('Partial Dependence Plots for macroInfo Features', fontsize=16)
    plt.tight_layout() 
    plt.savefig('./output/boosting/partial_dependence_macroInfo.png')
    print("Save figure ./output/boosting/partial_dependence_macroInfo.png")


@model_trainer
def train_xgboost(X_train, X_test, y_train, y_test, plot=False, save_model=False):
    parameters = {
        'max_depth': 5,
        'learning_rate': 0.1,
        'n_estimators': 1000,
        'objective': 'reg:squarederror',
        'subsample': 1,
        'colsample_bytree': 1,
        'reg_alpha': 1,
        'reg_lambda': 0.8
    }  # aae/pca reduced

    # parameters = {
    #     'max_depth': 5,
    #     'learning_rate': 0.1,
    #     'n_estimators': 1000,
    #     'objective': 'reg:squarederror',
    #     'subsample': 1,
    #     'colsample_bytree': 1,
    #     'reg_alpha': 1,
    #     'reg_lambda': 1
    # }  # unreduced

    model = XGBRegressor(**parameters)
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_pred = y_test_pred = model.predict(X_test)

    # train_mse = root_mean_squared_error(y_train, y_train_pred)
    # test_mse = root_mean_squared_error(y_test, y_test_pred)
    # train_r2 = r2_score(y_train, y_train_pred)
    # test_r2 = r2_score(y_test, y_test_pred)

    # print(f'Train RMSE: {train_mse:.4f}')
    # print(f'Test RMSE: {test_mse:.4f}')
    # print(f'Train R^2: {train_r2:.4f}')
    # print(f'Test R^2: {test_r2:.4f}')

    if plot:
        plot_summary(model, X_train)

    rmse = root_mean_squared_error(y_test, y_pred)
    print(f'RMSE: {rmse:.4f}')
    r2 = r2_score(y_test, y_pred)
    print(f'r2_score: {r2:.4f}')

    if save_model:
        if not os.path.exists("./saved_model"):
            os.mkdir("./saved_model")
        save_model_(model, './saved_model/xgboost.pkl')

    return model