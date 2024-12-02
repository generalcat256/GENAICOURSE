import os
import zipfile
import json

# Directory where the model files are stored or will be extracted
MODEL_DIR = "./trained_model5"
ZIP_FILE = "trained_model5.zip"  # Name of the zipped model file

def extract_model(zip_file=ZIP_FILE, extract_dir=MODEL_DIR):
    """
    Extract the model zip file if the directory does not exist.
    """
    if not os.path.exists(extract_dir):
        print("Extracting model files...")
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(extract_dir)
        print("Extraction complete.")
    else:
        print("Model files already extracted.")

def load_model(model_dir=MODEL_DIR):
    """
    Load the configuration and tokenizer from the model directory.
    """
    # Ensure the model is extracted
    extract_model()

    # Load the model configuration
    config_path = os.path.join(model_dir, "config.json")
    tokenizer_path = os.path.join(model_dir, "tokenizer.json")

    if not os.path.exists(config_path) or not os.path.exists(tokenizer_path):
        raise FileNotFoundError("Essential model files are missing.")

    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    print("Loaded model configuration:", config)

    with open(tokenizer_path, "r") as tokenizer_file:
        tokenizer = json.load(tokenizer_file)
    print("Loaded tokenizer configuration.")
    
    return config, tokenizer

def generate_text(description, model_dir=MODEL_DIR):
    """
    Generate Pokémon details dynamically based on the description and model configuration.
    """
    config, tokenizer = load_model(model_dir)  # Ensure model is loaded

    # Example of dynamic response based on description and model configuration
    types = config.get("types", ["Normal"])
    stats = {
        "HP": tokenizer.get("base_hp", 50) + len(description),
        "Attack": tokenizer.get("base_attack", 50) + len(description) % 10,
        "Defense": tokenizer.get("base_defense", 50) + len(description) % 5,
        "Speed": tokenizer.get("base_speed", 50) + len(description) % 20,
    }
    
    # Example Pokémon name generation based on description
    name = f"{description.split()[0].capitalize()}-mon" if description.strip() else "Mystery-mon"

    return {
        "Name": name,
        "Type": types[:2],  # Select up to 2 types
        "Stats": stats,
    }
