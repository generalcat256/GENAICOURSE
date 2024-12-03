from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import random

# Directory where the model files are stored
MODEL_DIR = "./trained_model5"

# Load the tokenizer and model
print("Loading tokenizer and model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)

# Define the valid Pokémon types
valid_types = [
    "Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting",
    "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
    "Dark", "Dragon", "Steel", "Fairy"
]

# Function to enforce valid Pokémon types
def enforce_valid_types(generated_output):
    # Handle Primary Type
    if "Type:" in generated_output:
        primary_type_start = generated_output.find("Type:") + 5
        primary_type_end = generated_output.find(";", primary_type_start)
        primary_type = generated_output[primary_type_start:primary_type_end].strip()

        if primary_type not in valid_types:
            random_primary_type = random.choice(valid_types)
            generated_output = generated_output.replace(f"Type: {primary_type}", f"Type: {random_primary_type}")
        else:
            random_primary_type = primary_type  # Keep the original if valid

    # Handle Secondary Type
    if "Secondary Type:" in generated_output:
        secondary_type_start = generated_output.find("Secondary Type:") + 15
        secondary_type_end = generated_output.find(";", secondary_type_start)
        secondary_type = generated_output[secondary_type_start:secondary_type_end].strip()

        if secondary_type not in valid_types and secondary_type != "None":
            valid_secondary_types = [t for t in valid_types if t != random_primary_type]
            random_secondary_type = random.choice(valid_secondary_types + ["None"])
            generated_output = generated_output.replace(
                f"Secondary Type: {secondary_type}", 
                f"Secondary Type: {random_secondary_type}"
            )
    return generated_output

# Function to enrich input for less detailed descriptions
def enrich_input(input_text):
    if len(input_text.split()) < 5:
        input_text += " with unique abilities and glowing features."
    return input_text

# Function to test the model with constrained types
def generate_with_constraints(input_text):
    input_text = enrich_input(input_text)  # Enrich input if needed
    print(f"Input Text (Enriched): {input_text}")

    # Tokenize the input text
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        max_length=64,
        truncation=True,
        padding="max_length"
    )

    # Generate outputs using temperature sampling
    outputs = model.generate(
        inputs["input_ids"],
        max_length=64,
        num_return_sequences=3,  # Generate 3 diverse outputs
        temperature=0.9,  # Higher temperature for more randomness
        top_k=10,  # Sample from top 10 tokens
        top_p=0.7,  # Nucleus sampling for diversity
        do_sample=True,  # Enable sampling
        repetition_penalty=2.0  # Penalize repetitive tokens
    )

    # Decode and enforce valid types in the generated outputs
    decoded_outputs = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    constrained_outputs = [enforce_valid_types(output) for output in decoded_outputs]
    return constrained_outputs

# Example usage
if __name__ == "__main__":
    example_input = "A spiky red Pokémon with bright eyes."
    outputs = generate_with_constraints(example_input)
    print("Generated Outputs:", outputs)
