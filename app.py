import streamlit as st
import pandas as pd
import random

# Define subdomains and descriptions
subdomains = [
    ("Cardiology", "The branch of medicine that deals with the disorders of the heart and circulatory system."),
    ("Neurology", "The study and treatment of disorders of the nervous system."),
    ("Pediatrics", "The branch of medicine that involves the medical care of infants, children, and adolescents."),
    ("Oncology", "The field of medicine dedicated to diagnosing, treating, and researching cancer."),
    ("Radiology", "The use of medical imaging to diagnose and treat diseases within the body."),
    ("Orthopedics", "The branch of medicine dealing with the correction of deformities of bones or muscles."),
    ("Dermatology", "The branch of medicine dealing with the skin, nails, hair, and their diseases."),
    ("Psychiatry", "The medical specialty devoted to the diagnosis, prevention, and treatment of mental disorders."),
    ("Endocrinology", "The branch of medicine dealing with the endocrine system, its diseases, and hormones."),
    ("Gastroenterology", "The branch of medicine focused on the digestive system and its disorders."),
]

# Create a DataFrame for the dataset
data = [{"Domain": "Medical", "Subdomain": sd[0], "Description": sd[1]} for sd in subdomains]
df = pd.DataFrame(data)

# Streamlit App
st.title("Domain Classification")
st.write("Enter a description to classify its domain and subdomain.")

# Text input for user
user_input = st.text_area("Enter a description:")

if user_input:
    # Find the best matching subdomain based on the description
    matched_row = df[df["Description"].str.contains(user_input, case=False, na=False)]

    if not matched_row.empty:
        matched_row = matched_row.iloc[0]
        st.subheader("Classification Result")
        st.write(f"**Domain:** {matched_row['Domain']}")
        st.write(f"**Subdomain:** {matched_row['Subdomain']}")
        st.write(f"**Description:** {matched_row['Description']}")
    else:
        st.subheader("No Match Found")
        st.write("Sorry, we couldn't classify the given description.")

# Display the entire dataset if requested
if st.checkbox("Show Complete Dataset"):
    st.dataframe(df)
