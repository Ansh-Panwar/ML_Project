import streamlit as st
from pages import Home, Dataset_Load, Train_Models, Upload_Predict, Visualization

# Set page config
st.set_page_config(
    page_title="ML Explorer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set Home as the default landing page
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Custom CSS for styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #1E1E2F;
        color: white;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45A049;
    }
    .main-title {
        font-size: 2rem;
        font-weight: bold;
        color: #333;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150", use_column_width=True)  # Placeholder for a logo
    st.title("🚀 ML Explorer")
    st.markdown("---")

    # Navigation
    page = st.radio(
        "Navigation",
        ["Home", "Dataset Load", "Train Models", "Upload & Predict", "Visualization"],
        index=0
    )

    # Store the selected page in session state
    st.session_state["page"] = page

    # Quick Tips
    st.markdown("""
    ### 🔥 Quick Tips
    - 📂 Load your dataset to get started
    - 🤖 Train ML models with a few clicks
    - 📊 Visualize model performance
    - 📤 Upload new data for predictions
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit</p>
        <p>Version 2.0.0</p>
    </div>
    """, unsafe_allow_html=True)

# Render the selected page
if st.session_state["page"] == "Home":
    Home.show()
elif st.session_state["page"] == "Dataset Load":
    Dataset_Load.show()
elif st.session_state["page"] == "Train Models":
    Train_Models.show()
elif st.session_state["page"] == "Upload & Predict":
    Upload_Predict.show()
elif st.session_state["page"] == "Visualization":
    Visualization.show()