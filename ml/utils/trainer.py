import time


def model_trainer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Finished {func.__name__}. ({end_time - start_time:.2f}s)\n")
        return result
    return wrapper

def get_params(model):
    print("Model Parameters:")
    for param, value in model.get_params().items():
        print(f"{param}: {value}")