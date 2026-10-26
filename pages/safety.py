import streamlit as st
import base64
import os
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Campus Safety & Security - ShuttleLyze",
    page_icon="🛡️",
    layout="wide"
)

# Helper function to convert local SVG to Base64 data URL
def get_svg_data_url(svg_path):
    if os.path.exists(svg_path):
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_content = f.read()
        b64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
        return f"data:image/svg+xml;base64,{b64}"
    return None

logo_svg_url = get_svg_data_url("C:/Users/ARYAN MAHAKUR/Downloads/lpu-logo.svg")

# 2. Custom CSS (Further reduced header size)
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff !important;
    }
    .stApp header {
        visibility: hidden;
        height: 0px;
    }
    [data-testid="stSidebar"] {
        display: none;
    }
    .block-container {
        padding-top: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        background-color: #ffffff !important;
    }
    
    /* Top Deep Maroon Banner */
    .top-banner {
        background-color: #800000;
        color: white;
        padding: 10px 30px;
        font-size: 13px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 500;
        display: flex;
        justify-content: space-between;
        align-items: center;
        letter-spacing: 0.5px;
    }
    
    .support-box {
        border: 1px solid white;
        padding: 5px 15px;
        font-size: 12px;
        letter-spacing: 0.5px;
    }

    /* Page Header Section (Scaled down to 17px) */
    .safety-header {
        border-bottom: 2px solid #800000;
        padding: 20px 60px 15px 60px;
        background-color: #ffffff;
    }
    .safety-title {
        color: #800000 !important;
        font-family: 'Georgia', serif;
        font-size: 17px;
        font-weight: bold;
        margin: 0;
    }
    
    /* Intro Description */
    .safety-intro {
        padding: 25px 60px 30px 60px;
        font-size: 15px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #333333;
        line-height: 1.6;
        max-width: 1100px;
    }
    
    /* Key Strategies Title Divider */
    .strategies-title-container {
        text-align: center;
        padding: 10px 0 30px 0;
    }
    .strategies-title {
        color: #333333;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 18px;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .strategies-divider {
        width: 80px;
        height: 2px;
        background-color: #444444;
        margin: 0 auto;
    }

    /* Expander Styling for High Contrast & Readability */
    [data-testid="stExpander"] {
        background-color: #fdfbfb !important;
        border: 1px solid #d0d0d0 !important;
        border-radius: 6px !important;
        margin-bottom: 12px !important;
    }
    [data-testid="stExpander"] summary p, 
    [data-testid="stExpander"] span {
        color: #222222 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    [data-testid="stExpander"] div[data-testid="stVerticalBlock"] p {
        color: #444444 !important;
        font-size: 14px !important;
        line-height: 1.5 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Top Deep Maroon Banner
st.markdown(
    '<div class="top-banner">'
    '<span>LOVELY PROFESSIONAL UNIVERSITY</span>'
    '<span class="support-box">24/7 CAMPUS SUPPORT +91 1824-444433 | 123 FROM CAMPUS PHONE</span>'
    '</div>', 
    unsafe_allow_html=True
)

# 4. Secondary Header Navigation Bar (Identical to Home Page)
logo_img_tag = f'<img src="{logo_svg_url}" style="height: 40px; margin-right: 15px; object-fit: contain;" alt="LPU Logo">' if logo_svg_url else '<div style="color: #800000; font-family: Georgia, serif; font-size: 24px; font-weight: bold; margin-right: 15px;">LPU</div>'

components.html(
    f"""
    <div style="background-color: #ffffff; border-bottom: 1px solid #e0e0e0; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; margin: 0;">
        <!-- Left Brand Logo & Title -->
        <div style="display: flex; align-items: center;">
            {logo_img_tag}
            <span style="color: #800000; font-family: 'Georgia', serif; font-size: 24px; font-weight: bold; letter-spacing: 0.5px;">SHUTTLELYZE</span>
        </div>
        
        <!-- Right Navigation Links -->
        <div style="display: flex; gap: 40px; align-items: center; font-size: 13px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">
            <a href="/safety" target="_self" style="color: #800000; text-decoration: none; font-weight: bold;">Safety Resources</a>
            <a href="/" target="_self" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">Services</a>
            <a href="/" target="_self" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">News & Alerts</a>
            <a href="/" target="_self" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">About</a>
            <a href="/" target="_self" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">Contact</a>
        </div>
    </div>
    """,
    height=75
)

# Main Title Header Section (Reduced to 17px)
st.markdown(
    """
    <div class="safety-header">
        <h1 class="safety-title">Lovely Professional University Safety & Security: Key Strategies</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Introductory paragraph
st.markdown(
    """
    <div class="safety-intro">
        The safety of people on campus and in the surrounding community is a paramount priority for Lovely Professional University. 
        The University and the Department of Safety & Security take a comprehensive approach to promoting safety. 
        On this page, you'll find a summary of our strategies.
    </div>
    """,
    unsafe_allow_html=True
)

# Key Strategies Header Section
st.markdown(
    """
    <div class="strategies-title-container">
        <div class="strategies-title">KEY STRATEGIES</div>
        <div class="strategies-divider"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# Centered container for the collapsible strategy list
_, content_col, _ = st.columns([0.1, 1.8, 0.1])

with content_col:
    with st.expander("LPU Campus Security Department"):
        st.write("LPU Campus Security operates 24/7 to patrol university grounds, secure academic/hostel zones, and respond immediately to student assistance calls and emergency triggers.")

    with st.expander("Campus and Neighborhood Security"):
        st.write("Comprehensive round-the-clock monitoring includes fixed security checkpoints, boundary patrols, and close coordination with local Phagwara law enforcement.")

    with st.expander("Transportation"):
        st.write("Free campus transit services, including Daytime Shuttles and NightRide vehicles up to 10:00 PM, equipped with panic alarm buttons and live CCTV feeds.")

    with st.expander("Campus-wide Technology"):
        st.write("Integration of modern surveillance systems, emergency blue-light call boxes, digital tracking via the LPU Golf Kart App, and automated access control.")

    with st.expander("Crime Communication and Reporting"):
        st.write("Transparent safety notices, prompt SMS/email emergency alerts, and secure online portals through UMS for reporting lost items or security incidents.")

    with st.expander("Community Collaboration"):
        st.write("Active student-faculty safety committees, awareness workshops, self-defense training sessions, and open feedback channels for continuous transit safety enhancement.")

    with st.expander("Support Resources"):
        st.write("Immediate 24/7 helpline access at +91 1824-444433 or shortcode 123 from any campus extension phone for counseling, escort services, and emergency response.")

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# 5. University Footer Section (Identical to Home Page)
components.html(
    """
    <div style="background-color: #800000; color: white; padding: 40px 50px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; margin-top: 40px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 30px; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 30px;">
            <div style="flex: 1; min-width: 250px;">
                <h3 style="color: white; font-family: 'Georgia', serif; margin-top: 0; font-size: 20px;">ShuttleLyze</h3>
                <p style="font-size: 13px; line-height: 1.6; color: #f0f0f0; margin-bottom: 0;">
                    Smart campus transportation analytics and route optimization system for Lovely Professional University. Ensuring safe and efficient transit across campus.
                </p>
            </div>
            <div style="flex: 1; min-width: 200px;">
                <h4 style="font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-top: 0; margin-bottom: 15px; color: #ffcccc;">Quick Links</h4>
                <ul style="list-style: none; padding: 0; margin: 0; font-size: 13px; line-height: 2; color: white;">
                    <li>Safety Resources</li>
                    <li>Campus Transportation</li>
                    <li>News & Alerts</li>
                    <li>About ShuttleLyze</li>
                </ul>
            </div>
            <div style="flex: 1; min-width: 250px;">
                <h4 style="font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-top: 0; margin-bottom: 15px; color: #ffcccc;">Contact Support</h4>
                <p style="font-size: 13px; line-height: 1.6; color: #f0f0f0; margin: 0;">
                    <b>Lovely Professional University</b><br>
                    Phagwara, Punjab, 144411, India<br>
                    Phone: +91 1824-444433 (Ext: 123)<br>
                    Email: support@lpu.co.in
                </p>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 20px; font-size: 12px; color: #dddddd; flex-wrap: wrap; gap: 10px;">
            <div>&copy; 2026 Lovely Professional University. All rights reserved. Developed for INT395-CA1-PROJECT.</div>
            <div>Privacy Policy &nbsp;|&nbsp; Terms of Service &nbsp;|&nbsp; Campus Security</div>
        </div>
    </div>
    """,
    height=260
)