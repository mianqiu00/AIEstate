import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import root_mean_squared_error, r2_score
import os
from tqdm import tqdm
from ml.utils import model_trainer, standard_scale, save_model_


class MLPModel(nn.Module):
    def __init__(self, input_dim):
        super(MLPModel, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )
    
    def forward(self, x):
        return self.layers(x)


@model_trainer
def train_mlp(X_train, X_test, y_train, y_test, epochs=250, batch_size=None, learning_rate=0.01, save_model=False):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    X_train, X_test = standard_scale(X_train, X_test)
    
    if batch_size:
        X_train_tensor = torch.tensor(X_train, dtype=torch.float32, batch_size=batch_size).to(device)
        X_test_tensor = torch.tensor(X_test, dtype=torch.float32, batch_size=batch_size).to(device)
        y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32, batch_size=batch_size).to(device)
        y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32, batch_size=batch_size).to(device)
    else:
        X_train_tensor = torch.tensor(X_train, dtype=torch.float32).to(device)
        X_test_tensor = torch.tensor(X_test, dtype=torch.float32).to(device)
        y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).to(device)
        y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).to(device)


    input_dim = X_train_tensor.shape[1]
    model = MLPModel(input_dim).to(device)
    
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    for epoch in tqdm(range(epochs), desc="Training Epoch: "):
        model.train()
        
        optimizer.zero_grad()
        outputs = model(X_train_tensor)
        loss = criterion(outputs.squeeze(), y_train_tensor)
        
        loss.backward()
        optimizer.step()
        
        # if (epoch + 1) % 10 == 0:
        #     print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')
    
    model.eval()
    with torch.no_grad():
        y_pred_tensor = model(X_test_tensor).squeeze()
        y_pred = y_pred_tensor.cpu().numpy()
        y_test = y_test_tensor.cpu().numpy()
        
        rmse = root_mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f'RMSE: {rmse:.4f}')
        print(f'R²: {r2:.4f}')

    if save_model:
        if not os.path.exists("./saved_model"):
            os.mkdir("./saved_model")
        save_model_(model, './saved_model/mlp.pkl')
    
    return model
