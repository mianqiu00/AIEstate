import dill

def save_model_(model, save_path):
    """
    Save the model to the specified path using dill.

    Parameters:
    - model: The model to be saved.
    - save_path: The path where the model will be saved.
    """
    try:
        with open(save_path, 'wb') as f:
            dill.dump(model, f)
        print(f"Model saved successfully to {save_path}")
    except Exception as e:
        print(f"Error saving model: {e}")
