import numpy as np
from src.ai_model import create_ai_model, train_model, predict_with_model

def main():
    # Example data and labels for training
    data = np.random.random((1000, 100))  # 1000 sample data points
    labels = np.random.randint(10, size=(1000,))  # Random labels between 0 and 9

    # Create AI model
    model = create_ai_model(input_shape=(100,))
    
    # Train the model
    train_model(model, data, labels)
    
    # Make predictions with the model
    predictions = predict_with_model(model, data[:5])
    print(f"Predictions: {predictions}")

if __name__ == "__main__":
    main()
