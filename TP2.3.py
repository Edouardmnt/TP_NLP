import kagglehub

# Download latest version
path = kagglehub.dataset_download("vbmokin/nlp-with-disaster-tweets-cleaning-data")

print("Path to dataset files:", path)