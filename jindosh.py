import streamlit as st
import pandas as pd

# Title of the application
st.title("Jindosh Riddle Solution Tool")

# Prompts for user input (modified for dropdowns where necessary)
prompts = [
    "Please enter the first name on line 4.",
    "Please enter the second name on line 4.",
    "Please select the heirloom on line 9.",  # Dropdown for heirlooms
    "Please enter the name from line 11.",
    "Please select the heirloom from line 11.",  # Dropdown for heirlooms
    "Please select the heirloom from line 12.",  # Dropdown for heirlooms
    "Please select the heirloom from line 13.",  # Dropdown for heirlooms
    "Please enter the name from line 15.",
    "Please enter the name from line 17."
]

# List of heirlooms
all_heirlooms = ["Snuff Tin", "War Medal", "Bird Pendant", "Ring", "Diamond"]

# Create an empty table with two rows and five columns
table = pd.DataFrame(
    [[''] * 5, [''] * 5],
    index=["Names", "Heirlooms"],
    columns=["A", "B", "C", "D", "E"]
)

# Mapping user inputs to specific cells in the table
cell_mapping = {
    0: ("Names", "E"),  # Prompt 1 -> A5
    1: ("Names", "A"),  # Prompt 2 -> A1
    2: ("Heirlooms", "B"),  # Prompt 3 -> B2 (Dropdown for heirloom)
    3: ("Names", "D"),  # Prompt 4 -> A4
    4: ("Heirlooms", "D"),  # Prompt 5 -> B4 (Dropdown for heirloom)
    5: ("Heirlooms", "E"),  # Prompt 6 -> B5 (Dropdown for heirloom)
    6: ("Heirlooms", "A"),  # Prompt 7 -> B1 (Dropdown for heirloom)
    7: ("Names", "B"),  # Prompt 8 -> A2
    8: ("Names", "C")   # Prompt 9 -> A3
}

# Collect user inputs
user_inputs = {}  # To keep track of selected heirlooms

for i, prompt in enumerate(prompts):
    if i in [2, 4, 5, 6]:  # For heirloom selection prompts
        user_input = st.selectbox(prompt, options=all_heirlooms, key=f"input_{i}")
        user_inputs[f"heirloom_{i}"] = user_input  # Store the selected heirloom
    else:  # For name input prompts
        user_input = st.text_input(prompt, key=f"input_{i}")
    
    if user_input:
        row, col = cell_mapping[i]
        table.at[row, col] = user_input

# Add a button to generate the solution table
if st.button("Generate Solution"):
    # Find which heirloom is missing by comparing the selected heirlooms to the full list
    selected_heirlooms = set(user_inputs.values())
    missing_heirloom = list(set(all_heirlooms) - selected_heirlooms)[0]  # Find the missing heirloom
    
    # Find the empty cell in row "Heirlooms" (row B) and fill it with the missing heirloom
    for col in table.columns:
        if table.at["Heirlooms", col] == '':  # Find the empty heirloom cell
            table.at["Heirlooms", col] = missing_heirloom
            break  # Only fill one cell

    # Display the final table with larger font size using CSS
    st.write("### Jindosh Riddle Solution:")

    # Apply custom CSS to increase the font size of the table
    st.markdown(
        """
        <style>
        .streamlit-expanderHeader {
            font-size: 24px !important;
        }
        table {
            font-size: 20px !important;
        }
        </style>
        """, unsafe_allow_html=True)

    # Display the table with the custom font size
    st.dataframe(table)

    # Add the attribution link below the table
    st.markdown(
        """
        **Thanks to Steam user ["Nate Dies A Lot"](https://steamcommunity.com/sharedfiles/filedetails/?id=799586506) for providing the solution steps for this code.
        """)
    st.markdown(
        """
        **Thanks to Arkane Studios for one of the best games ever made.
        """)
    st.markdown(
        """
        **For any changes, questions, or comments, please send an email to imjoshwa@live.com.
        """)
