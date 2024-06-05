import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(layout="wide")

# Title of the website
st.title("✨ HR Executive Summary Dashboard 📊")

# File uploader for users to upload their own data
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

def download_button(fig, chart_name, type):
    # Save the pie chart to a BytesIO object
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
        
    # Download button
    st.download_button(
        label=f"Download {chart_name}_{type}_chart.png",
        data=buf,
        file_name=f"{chart_name}_{type}_chart.png",
        mime="image/png"
    )

def s1_dashboard(df, chart_name, label_viz):
    # Title    
    st.write(df)

    # Default colors for pie chart
    default_colors = ["#ff9999", "#66b3ff", "#99ff99"]

    # Color pickers for each segment of the pie chart
    colors = []
    for i, label in enumerate(df['STATUS']):
        color = st.color_picker(f"Pick a color for {label}", value=default_colors[i])
        colors.append(color)

    # if select bar
    if label_viz == 'bar':
        fig, ax = plt.subplots()
        ax.bar(df['STATUS'], df['COUNT'], label=df['STATUS'], color=colors)
        st.pyplot(fig)
        # Save the bar chart to a BytesIO object
        download_button(fig, chart_name, label_viz)

    # else select pie
    else:
        fig, ax = plt.subplots()
        ax.pie(df['COUNT'], labels=df['STATUS'], colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
        st.pyplot(fig)
        # Save the pie chart to a BytesIO object
        download_button(fig, chart_name, label_viz)

def s2_dashboard(df, chart_name, label_viz):
    # Title    
    st.write(df)
        
    # Default colors for pie chart
    default_colors = ["#ff9999", "#66b3ff", "#99ff99"]

    # Color pickers for each segment of the pie chart
    colors = []
    for i, label in enumerate(df['CLUSTER_PERFORMANCE_AI']):
        color = st.color_picker(f"Pick a color for {label}", value=default_colors[i])
        colors.append(color)
    
    # if select bar
    if label_viz == 'bar':
        fig, ax = plt.subplots()
        ax.bar(df['CLUSTER_PERFORMANCE_AI'], df['COUNT'], label=df['CLUSTER_PERFORMANCE_AI'], color=colors)
        st.pyplot(fig)
        # Save the bar chart to a BytesIO object
        download_button(fig, chart_name, label_viz)

    # else select pie
    else:
        fig, ax = plt.subplots()
        ax.pie(df['COUNT'], labels=df['CLUSTER_PERFORMANCE_AI'], colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
        st.pyplot(fig)
        # Save the pie chart to a BytesIO object
        download_button(fig, chart_name, label_viz)

def s3_dashboard(df, chart_name, label_viz):
    # Title    
    st.write(df)

    # Default colors for pie chart
    default_colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffe280"]

    # Color pickers for each segment of the pie chart
    colors = []
    for i, label in enumerate(df['TALENT_TRACK']):
        color = st.color_picker(f"Pick a color for {label}", value=default_colors[i])
        colors.append(color)

    # if select bar
    if label_viz == 'bar':
        fig, ax = plt.subplots()
        ax.bar(df['TALENT_TRACK'], df['COUNT'], label=df['TALENT_TRACK'], color=colors)
        st.pyplot(fig)
        # Save the bar chart to a BytesIO object
        download_button(fig, chart_name, label_viz)

    # else select pie
    else:
        fig, ax = plt.subplots()
        ax.pie(df['COUNT'], labels=df['TALENT_TRACK'], colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
        st.pyplot(fig)
        # Save the pie chart to a BytesIO object
        download_button(fig, chart_name, label_viz)

def s4_dashboard(df, chart_name, label_viz):
    # Title    
    st.write(df)

    # Default colors for pie chart
    default_colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffe280", "#9061f9"]

    # Color pickers for each segment of the pie chart
    colors = []
    for i, label in enumerate(df['TIER_TRACK']):
        color = st.color_picker(f"Pick a color for {label}", value=default_colors[i])
        colors.append(color)

    # if select bar
    if label_viz == 'bar':
        fig, ax = plt.subplots()
        ax.bar(df['TIER_TRACK'], df['COUNT'], label=df['TIER_TRACK'], color=colors)
        st.pyplot(fig)
        # Save the bar chart to a BytesIO object
        download_button(fig, chart_name, label_viz)

    # else select pie
    else:
        fig, ax = plt.subplots()
        ax.pie(df['COUNT'], labels=df['TIER_TRACK'], colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
        st.pyplot(fig)
        # Save the pie chart to a BytesIO object
        download_button(fig, chart_name, label_viz)

# Customize page
def intro():
    st.write("# Welcome HR team! 👋")
    st.markdown(f"""
        ### Information of your file is shown below 📁
        1. Filename: **{uploaded_file.name}** 
        2. Company: **{uploaded_file.name.split("_")[5:-2]}** 
        3. Year: **{uploaded_file.name.split("_")[-2]}** 
        4. AI running date: **{uploaded_file.name.split("_")[-1].split(".")[0]}** 

        ### Select a dashboard from the dropdown on the left 📈
        1. Participant Information dashboard
        2. Talent Identification Result by AI
        3. Talent track by AI
        4. Talent tier by AI
        5. Top Talent Recommendation by AI

        ### Customize, ALL-YOU-WANT 🎨
        1. Select Bar chart for comparison by values
        2. Select Pie chart for comparison by percentage
        3. Change the color in chart
        4. Download for your internal report
    """)

def participant_information():
    # Get data
    df_1 = pd.read_excel(uploaded_file, sheet_name='ref_number_candidate')

    # Get header
    st.header("Section 1: Participant Information")

    label_viz = st.sidebar.radio("Select Chart Type", options=["bar", "pie"], index=0)

    s1_dashboard(df=df_1, chart_name="participant_information", label_viz=label_viz)

def talent_identification_result_ai():
    # Get data
    df_2 = pd.read_excel(uploaded_file, sheet_name='ref_ai_clustering')

    # Get header
    st.header("Section 2: Talent Identification Result by AI")

    label_viz = st.sidebar.radio("Select Chart Type", options=["bar", "pie"], index=0)

    s2_dashboard(df=df_2, chart_name="talent_identification_result_ai", label_viz=label_viz)

def talent_track_ai():
    # Get data
    df_3 = pd.read_excel(uploaded_file, sheet_name='ref_ai_talent_track')

    # Get header
    st.header("Section 3: Talent Identification Result by AI")

    label_viz = st.sidebar.radio("Select Chart Type", options=["bar", "pie"], index=0)

    s3_dashboard(df=df_3, chart_name="talent_track_ai", label_viz=label_viz)

def talent_tier_ai():
    # Get data
    df_4 = pd.read_excel(uploaded_file, sheet_name='ref_ai_tier')

    # Get header
    st.header("Section 4: Talent Tier Result by AI")

    label_viz = st.sidebar.radio("Select Chart Type", options=["bar", "pie"], index=0)

    s4_dashboard(df=df_4, chart_name="talent_tier_ai", label_viz=label_viz)

def toptalent_rec_ai():
    # Get data
    df_5 = pd.read_excel(uploaded_file, sheet_name='ref_ai_recommendation')

    # Get header
    st.header("Section 5: Top talent recommedation from AI")

    st.dataframe(df_5, use_container_width=True)


if __name__ == "__main__":
    if uploaded_file is not None:
        page_names_to_funcs = {
            "—": intro,
            "Participant Information": participant_information,
            "Talent Identification Result by AI": talent_identification_result_ai,
            "Talent track by AI": talent_track_ai,
            "Talent tier by AI": talent_tier_ai,
            "Top Talent Recommendation": toptalent_rec_ai
        }

        try:
            # Default showing 
            demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
            page_names_to_funcs[demo_name]()

        except Exception as e:
            st.write(f":red[Oops🤫, something went wrong!] \n>> {e}")

    else: 
        st.markdown("##### Please upload 🚀 **The EXECUTIVE_SUMMARY_RAW_DATA.xlsx** ")
