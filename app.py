import streamlit as st

# Title and description of the app
st.title("Pokémon Generator")
st.markdown("Enter a Pokémon description below to generate a new Pokémon with an image, name, types, and stats!")

# Input field for Pokémon description
description = st.text_input("Describe your Pokémon:", placeholder="e.g., A fiery bird with blue flames, agile and brave.")

# Placeholder data to simulate outputs
placeholder_image = "https://via.placeholder.com/512"  # Placeholder image URL
placeholder_text_output = {
    "Name": "Flarehawk",
    "Type": ["Fire", "Flying"],
    "Stats": {
        "HP": 78,
        "Attack": 84,
        "Defense": 78,
        "Speed": 100,
    },
}

# Display results if a description is entered
if description:
    st.markdown("### Generating Pokémon...")

    # Simulate generated image
    st.image(placeholder_image, caption="Generated Pokémon Image", use_column_width=True)

    # Display placeholder details
    st.markdown("### Pokémon Details")
    st.write(f"**Name**: {placeholder_text_output['Name']}")
    st.write(f"**Type(s)**: {', '.join(placeholder_text_output['Type'])}")
    st.write("**Stats**:")
    for stat, value in placeholder_text_output["Stats"].items():
        st.write(f"- {stat}: {value}")
