from sklearn.preprocessing import MinMaxScaler, StandardScaler


def min_max_scale(train, test):
    scaler = MinMaxScaler()
    
    train_scaled = scaler.fit_transform(train)
    test_scaled = scaler.transform(test)
    
    return train_scaled, test_scaled


def standard_scale(train, test):
    scaler = StandardScaler()
    
    train_scaled = scaler.fit_transform(train)
    test_scaled = scaler.transform(test)
    
    return train_scaled, test_scaled
