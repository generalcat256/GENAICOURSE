import streamlit as st
from models.image_model import generate_image
from models.text_model import generate_text

# Title and description
st.title("Pokémon Generator")
st.markdown("Enter a Pokémon description to generate a new Pokémon with a name, type, and stats!")

# Input field
description = st.text_input("Describe your Pokémon:", placeholder="e.g., A fiery bird with blue flames, agile and brave.")

if description:
    # Generate outputs
    with st.spinner("Generating Pokémon..."):
        image = generate_image(description)  # Call to your image model
        text_output = generate_text(description)  # Call to your text-to-text model

    # Display outputs
    st.image(image, caption="Generated Pokémon Image", use_column_width=True)
    st.write("### Pokémon Details")
    st.write(text_output)
