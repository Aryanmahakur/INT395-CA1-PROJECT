import streamlit as strlit

# Page Configuration
strlit.set_page_config(
    page_title="ShuttleSis - Campus Transport & Demand Optimization",
    page_icon="🚌",
    layout="wide"
)

# Custom CSS for styling
strlit.markdown("""
    <style>
    .hero-container {
        background-color: #ffffff;
        padding: 3rem 2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-top: 2rem;
    }
    .hero-title {
        color: #1e40af;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .hero-description {
        color: #475569;
        font-size: 1.15rem;
        max-width: 800px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Top Navigation Bar using Columns
col1, col2, col3, col4 = strlit.columns([4, 1, 1, 1])

with col1:
    strlit.markdown("### 🚌 **shuttlesis**")

# Using session state or simple selectbox/radio for navigation tabs in the header area
nav_selection = strlit.radio(
    "Navigation", 
    ["Home", "Services", "About Us"], 
    horizontal=True, 
    label_visibility="collapsed"
)

strlit.divider()

# Page Content Routing
if nav_selection == "Home":
    # Hero Section
    strlit.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Intelligent Campus Transportation & Demand Optimization</h1>
            <p class="hero-description">
                Welcome to <strong>ShuttleSis</strong>. This platform is an advanced machine learning-driven system 
                engineered to predict passenger transit demand, optimize campus shuttle routes, minimize wait times, 
                and streamline traffic flow efficiently across the campus ecosystem.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    strlit.write("")
    strlit.write("")
    
    # Quick Metrics / Feature Preview Cards
    c1, c2, c3 = strlit.columns(3)
    with c1:
        strlit.info("📈 **Demand Prediction**\n\nForecast passenger volumes using trained ML regression models based on time, weather, and campus events.")
    with c2:
        strlit.success("🗺️ **Route Optimization**\n\nMinimize transit delays and optimize vehicle deployment across key campus stops.")
    with c3:
        strlit.warning("⚡ **Real-time Analytics**\n\nMonitor live shuttle movement and system bottlenecks through interactive dashboards.")

elif nav_selection == "Services":
    strlit.header("Our Services")
    strlit.write("Explore the core modules built into the ShuttleSis platform:")
    strlit.markdown("- **Passenger Demand Forecasting Dashboard**")
    strlit.markdown("- **Shuttle Route & Schedule Simulator**")
    strlit.markdown("- **Wait-Time Analytics Engine**")

elif nav_selection == "About Us":
    strlit.header("About ShuttleSis")
    strlit.write("ShuttleSis is developed as an intelligent campus mobility solution designed to streamline daily transit logistics, reduce congestion, and improve operational efficiency for university transport systems.")