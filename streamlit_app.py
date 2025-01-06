import streamlit as st
import pandas as pd

# Title of the application
st.title("Jindosh Riddle Solution Tool")

# Prompts for user input
prompts = [
    "Please enter the first name on line 4.",
    "Please enter the second name on line 4.",
    "Please enter the heirloom on line 9.",
    "Please enter the name from line 11.",
    "Please enter the heirloom from line 11.",
    "Please enter the heirloom from line 12.",
    "Please enter the heirloom from line 13.",
    "Please enter the name from line 15.",
    "Please enter the name from line 17."
]

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
    2: ("Heirlooms", "B"),  # Prompt 3 -> B2
    3: ("Names", "D"),  # Prompt 4 -> A4
    4: ("Heirlooms", "D"),  # Prompt 5 -> B4
    5: ("Heirlooms", "E"),  # Prompt 6 -> B5
    6: ("Heirlooms", "A"),  # Prompt 7 -> B1
    7: ("Names", "B"),  # Prompt 8 -> A2
    8: ("Names", "C")   # Prompt 9 -> A3
}

# Collect user inputs
for i, prompt in enumerate(prompts):
    user_input = st.text_input(prompt, key=f"input_{i}")
    if user_input:
        row, col = cell_mapping[i]
        table.at[row, col] = user_input

# Add a button to generate the solution table
if st.button("Generate Solution Table"):
    # Automatically fill the last empty cell with "Bird Pendant"
    if '' in table.values:
        empty_cell = table.stack()[table.stack() == ''].index[0]  # Find the first empty cell
        table.at[empty_cell] = "Bird Pendant"

    # Display the final table with larger font size using CSS
    st.write("### Solved Jindosh Riddle Table:")

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