import pandas as pd

# Example synthetic data
features = [
    [0.5, 0.8, 0.3],
    [0.2, 0.4, 0.7],
    [0.9, 0.1, 0.6]
]
labels = [1, 0, 1]  # Well-connected or poorly connected

# Save features and labels
pd.DataFrame(features, columns=["feature1", "feature2", "feature3"]).to_csv("data/synthetic_features.csv", index_label="location_id")
pd.DataFrame(labels, columns=["label"]).to_csv("data/labels.csv", index_label="location_id")
