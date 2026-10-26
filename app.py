import streamlit as st
import base64
import os
import streamlit.components.v1 as components

# 1. Page Configuration (Must be first Streamlit command)
st.set_page_config(
    page_title="ShuttleLyze",
    page_icon="🚌",
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

# 2. Custom CSS (Includes Fix for Expander Visibility)
st.markdown("""
<style>
    /* Force main app background to pure white shade */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* Remove default Streamlit top header whitespace & hide sidebar nav entirely */
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

    /* Hero Section */
    .hero-container {
        background-color: #f8f9fa;
        padding: 50px 40px;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .hero-heading {
        color: #800000;
        font-family: 'Georgia', serif;
        font-size: 34px;
        font-weight: bold;
        margin-top: 0px;
        margin-bottom: 16px;
        letter-spacing: 0.5px;
    }
    
    .hero-text {
        font-size: 14px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        line-height: 1.6;
        color: #666666;
        font-weight: 400;
        max-width: 900px;
    }

    /* Centered Section Styling */
    .centered-section {
        text-align: center;
        padding: 50px 20px 20px 20px;
        background-color: #ffffff;
    }

    .centered-title {
        color: #333333;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 22px;
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .centered-divider {
        width: 80px;
        height: 2px;
        background-color: #444444;
        margin: 0 auto 20px auto;
    }

    .centered-description {
        color: #555555;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 15px;
        line-height: 1.6;
        max-width: 800px;
        margin: 0 auto;
    }

    /* Fix Expander Text and Background Contrast */
    [data-testid="stExpander"] {
        background-color: #fdfbfb !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 6px !important;
        margin-bottom: 10px !important;
    }
    [data-testid="stExpander"] summary p, 
    [data-testid="stExpander"] span {
        color: #333333 !important;
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

# Query parameter router to handle single-page navigation seamlessly
query_params = st.query_params
current_page = query_params.get("page", "home")

# 3. Top Deep Maroon Banner
st.markdown(
    '<div class="top-banner">'
    '<span>LOVELY PROFESSIONAL UNIVERSITY</span>'
    '<span class="support-box">24/7 CAMPUS SUPPORT +91 1824-444433 | 123 FROM CAMPUS PHONE</span>'
    '</div>', 
    unsafe_allow_html=True
)
# 4. Secondary Header Navigation Bar with Clean White Background & Spacing
logo_img_tag = f'<img src="{logo_svg_url}" style="height: 40px; margin-right: 15px; object-fit: contain;" alt="LPU Logo">' if logo_svg_url else '<div style="color: #800000; font-family: Georgia, serif; font-size: 24px; font-weight: bold; margin-right: 15px;">LPU</div>'

components.html(
    f"""
    <div style="background-color: #ffffff; border-bottom: 1px solid #e0e0e0; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; margin: 0;">
        <!-- Left Brand Logo & Title -->
        <div style="display: flex; align-items: center;">
            {logo_img_tag}
            <span style="color: #800000; font-family: 'Georgia', serif; font-size: 24px; font-weight: bold; letter-spacing: 0.5px;">SHUTTLELYZE</span>
        </div>
        
        <!-- Right Navigation Links: target="_blank" opens safety in a separate browser window/tab -->
        <div style="display: flex; gap: 40px; align-items: center; font-size: 13px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">
            <a href="/safety" target="_blank" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">Safety Resources</a>
            <a href="/" target="_self" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">Services</a>
            <a href="/" target="_self" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">News & Alerts</a>
            <a href="/" target="_self" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">About</a>
            <a href="/" target="_self" style="color: #444444; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#800000'" onmouseout="this.style.color='#444444'">Contact</a>
        </div>
    </div>
    """,
    height=75
)
# --- PAGE ROUTING LOGIC ---
if current_page == "safety":
    safety_file_path = "C:/Users/ARYAN MAHAKUR/Desktop/VS CODE/INT395-CA1-PROJECT/pages/safety.py"
    if os.path.exists(safety_file_path):
        with open(safety_file_path, "r", encoding="utf-8") as f:
            safety_code = f.read()
        exec(safety_code, globals())
    else:
        st.error(f"Could not find safety file at: {safety_file_path}")
else:
    # HOME / OVERVIEW LANDING PAGE CONTENT
    st.markdown(
        '<div class="hero-container">'
        '<div class="hero-heading">Shuttle Services</div>'
        '<div class="hero-text">'
        'The ShuttleLyze Program is a free campus transportation service provided by Lovely Professional University. '
        'Daytime Shuttles and NightRide Shuttles travel on and around the greater campus area. '
        'The shuttles run year-round, except on University-observed holidays. To ride the shuttles, passengers '
        'are asked to tap a valid University-issued ID when boarding.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="centered-section">'
        '<div class="centered-title">TRANSPORTATION AT LOVELY PROFESSIONAL UNIVERSITY</div>'
        '<div class="centered-divider"></div>'
        '<div class="centered-description">'
        'Having reliable transportation options is an important part of staying safe. We have many ways to move safely around campus and the Phagwara area. '
        'See the map for shuttle, train, and bus routes, EV bike sharing locations, and campus parking lots.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # University Route Map Section
    st.markdown('<div style="padding: 20px 40px 50px 40px; background-color: #ffffff;">', unsafe_allow_html=True)
    _, center_container, _ = st.columns([0.15, 1.7, 0.15])

    with center_container:
        col_routes, col_map = st.columns([1, 1.2], gap="large")

        with col_routes:
            st.markdown(
                """
                <h3 style="color: #800000; font-family: 'Georgia', serif; font-size: 22px; margin-bottom: 15px;">
                    LPU Campus Shuttle Routes
                </h3>
                <div style="font-size: 14px; color: #333333; line-height: 2.2; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">
                    <label style="display: block; cursor: pointer; border-bottom: 1px solid #eee; padding-bottom: 5px;">
                        <input type="checkbox" checked="checked" style="accent-color: #800000; margin-right: 8px;"> <b>Block 1 to Block 57 Route</b><br>
                        <span style="color: #666; font-size: 12px; margin-left: 20px;">Distance: 1,451.1 m | Avg Time: ~12 min</span>
                    </label>
                    <label style="display: block; cursor: pointer; border-bottom: 1px solid #eee; padding-top: 8px; padding-bottom: 5px;">
                        <input type="checkbox" checked="checked" style="accent-color: #800000; margin-right: 8px;"> <b>Block 1 to Block 73 Route</b><br>
                        <span style="color: #666; font-size: 12px; margin-left: 20px;">Distance: 1,620.0 m | Avg Time: ~14 min</span>
                    </label>
                    <label style="display: block; cursor: pointer; border-bottom: 1px solid #eee; padding-top: 8px; padding-bottom: 5px;">
                        <input type="checkbox" checked="checked" style="accent-color: #800000; margin-right: 8px;"> <b>Block 1 to Block 48 Route</b><br>
                        <span style="color: #666; font-size: 12px; margin-left: 20px;">Distance: 1,180.5 m | Avg Time: ~9 min</span>
                    </label>
                    <label style="display: block; cursor: pointer; padding-top: 8px;">
                        <input type="checkbox" checked="checked" style="accent-color: #800000; margin-right: 8px;"> <b>Block 1 to Block 25 Route</b><br>
                        <span style="color: #666; font-size: 12px; margin-left: 20px;">Distance: 885.2 m | Avg Time: ~7 min</span>
                    </label>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col_map:
            components.html(
                """
                <div style="border: 2px solid #800000; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13715.1798369524!2d75.7001!3d31.2530!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391a5f5e9c0c0c0d%3A0x7c7c7c7c7c7c7c7c!2sLovely%20Professional%20University!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" width="100%" height="320" style="border:0; display: block;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
                </div>
                """,
                height=330,
            )
    st.markdown('</div>', unsafe_allow_html=True)

    # LPU Shuttle Basics Section
    st.markdown('<div style="padding: 30px 40px 50px 40px; background-color: #ffffff;">', unsafe_allow_html=True)
    _, center_container_basics, _ = st.columns([0.15, 1.7, 0.15])

    with center_container_basics:
        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 22px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;">
                    We Know You Have Question's Right?
                </div>
                <div style="width: 80px; height: 2px; background-color: #444444; margin: 0 auto;"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("Daytime Shuttle Schedule"):
            st.write("Daytime shuttles operate from 8:00 AM to 10:00 AM, Monday to Sunday.")

        with st.expander("NightRide Shuttle Schedule"):
            st.write("NightRide shuttle operations continue until 10:00 PM.")

        with st.expander("Tracking the movement of UGo Shuttles"):
            st.write("You can use the LPU Golf Kart App for real-time tracking of shuttle movements across campus.")

        with st.expander("Give feedback"):
            st.write("Feedback options are available both on this website/portal and directly within the LPU Golf Kart App.")

        with st.expander("Lost and Found"):
            st.write("For any lost and found queries or reporting missing items, please visit ums.lpu.in.")

        with st.expander("Using your ID to ride UGo shuttles"):
            st.write("To ride UGo shuttles, simply ask the driver for ID verification and make the payment.")

        with st.expander("How to request a Safety Escort"):
            st.write("Each vehicle is equipped with an emergency alarm button and CCTV cameras for security. You can trigger the alarm or contact campus safety directly for immediate assistance.")

    st.markdown('</div>', unsafe_allow_html=True)

    # University Footer Section
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