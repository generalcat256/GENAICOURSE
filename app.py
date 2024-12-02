import streamlit as st
import os
import zipfile
import json

# Paths for the model files
MODEL_DIR = "./trained_model5"
ZIP_FILE = "trained_model5.zip"

def extract_model(zip_file=ZIP_FILE, extract_dir=MODEL_DIR):
    """
    Extract the model zip file if the directory does not exist.
    """
    if not os.path.exists(extract_dir):
        st.info("Extracting model files... Please wait.")
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(extract_dir)
        st.success("Extraction complete.")
    else:
        st.info("Model files already extracted.")

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
        st.error("Essential model files are missing. Please check your setup.")
        raise FileNotFoundError("Essential model files are missing.")

    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    with open(tokenizer_path, "r") as tokenizer_file:
        tokenizer = json.load(tokenizer_file)

    return config, tokenizer

def generate_text(description, model_dir=MODEL_DIR):
    """
    Generate Pokémon details based on the description.
    """
    # Load model (simulated for now)
    config, tokenizer = load_model(model_dir)

    # Placeholder logic for now
    st.info(f"Using config: {config['model_name']}")
    return {
        "Name": "Simula-mon",
        "Type": ["Psychic", "Electric"],
        "Stats": {
            "HP": 90,
            "Attack": 80,
            "Defense": 75,
            "Speed": 110,
        },
    }

# Title and description of the app
st.title("Pokémon Generator")
st.markdown("Enter a Pokémon description to generate a name, type, and stats!")

# Input field for Pokémon description
description = st.text_input("Describe your Pokémon:", placeholder="e.g., A fiery bird with blue flames.")

if description:
    st.markdown("### Generating Pokémon...")

    # Generate Pokémon details
    try:
        text_output = generate_text(description)

        # Display results
        st.write("### Pokémon Details")
        st.write(f"**Name**: {text_output['Name']}")
        st.write(f"**Type(s)**: {', '.join(text_output['Type'])}")
        st.write("**Stats**:")
        for stat, value in text_output["Stats"].items():
            st.write(f"- {stat}: {value}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
