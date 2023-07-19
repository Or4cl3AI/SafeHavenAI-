```python
import os
import json

USER_TRAINING_DATA = {}

def train_user():
    # Load training data
    with open('training_data.json', 'r') as file:
        training_data = json.load(file)

    # Iterate over the training data and educate the user
    for topic, content in training_data.items():
        print(f"Topic: {topic}")
        print(f"Content: {content}")
        USER_TRAINING_DATA[topic] = content

    # Save the user training data for reporting
    with open('user_training_data.json', 'w') as file:
        json.dump(USER_TRAINING_DATA, file)

    print("User training completed successfully.")

if __name__ == "__main__":
    train_user()
```