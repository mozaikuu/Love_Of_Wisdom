import random
import pandas as pd

# Simulate reaction times and logs for 500000 entries
data_simulated_large = {

    "reaction_speed(in_ms)_tot": [sum([random.randint(0, 1000) for _ in range(50000)]) for _ in range(500)],

}

# Create a DataFrame
updated_data_large = pd.DataFrame(data_simulated_large)

# Save the larger dataset to the file
updated_large_file_path = './Datasets/ND(50000)_dataset.csv'
updated_data_large.to_csv(updated_large_file_path, index=False)

# Display the first few rows of the updated dataset
updated_data_large.head(), updated_large_file_path