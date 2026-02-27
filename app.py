import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="Tyre Formatter", layout="wide")

# -------------------- Custom CSS for Elderly-Friendly UI --------------------
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #f0f4f8;
    }
    
    /* Large, readable title */
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: #1a5276;
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 1.5rem;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a5276;
        padding: 1rem 0;
        border-bottom: 4px solid #2980b9;
        margin: 2rem 0 1.5rem 0;
    }
    
    /* Radio button container */
    .stRadio > div {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Radio button labels - LARGER and DARKER */
    .stRadio label {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #1a1a1a !important;
    }
    
    .stRadio p {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #1a1a1a !important;
    }
    
    .stRadio div[data-testid="stMarkdownContainer"] p {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #1a1a1a !important;
    }
    
    /* File uploader styling */
    .stFileUploader {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .stFileUploader label {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        color: #1a1a1a !important;
    }
    
    /* File uploader dropzone - FIX VISIBILITY */
    .stFileUploader section {
        background-color: #e8f4fc !important;
        border: 3px dashed #2980b9 !important;
        border-radius: 12px !important;
    }
    
    .stFileUploader section > div {
        background-color: transparent !important;
    }
    
    /* Drag and drop text */
    .stFileUploader section span {
        color: #1a5276 !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
    }
    
    .stFileUploader section small {
        color: #34495e !important;
        font-size: 1.1rem !important;
    }
    
    /* Browse files button */
    .stFileUploader section button {
        background-color: #2980b9 !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        padding: 0.8rem 1.5rem !important;
        border-radius: 8px !important;
        border: none !important;
    }
    
    .stFileUploader section button:hover {
        background-color: #1a5276 !important;
    }
    
    /* Uploaded file name */
    .stFileUploader [data-testid="stFileUploaderFile"] {
        background-color: #ffffff !important;
    }
    
    .stFileUploader [data-testid="stFileUploaderFile"] span {
        color: #1a1a1a !important;
        font-size: 1.2rem !important;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background-color: #27ae60 !important;
        color: white !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        padding: 1rem 2.5rem !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(39, 174, 96, 0.3) !important;
    }
    
    .stDownloadButton > button:hover {
        background-color: #219a52 !important;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Success messages */
    .stSuccess {
        font-size: 1.3rem !important;
        border-radius: 10px !important;
    }
    
    .stSuccess p {
        font-size: 1.3rem !important;
        color: #155724 !important;
    }
    
    /* All headers */
    h1, h2, h3 {
        color: #1a5276 !important;
        font-weight: 700 !important;
    }
    
    /* General text - MUCH LARGER */
    p, span, label, div {
        font-size: 1.3rem !important;
        line-height: 1.8 !important;
        color: #1a1a1a !important;
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 3px;
        background-color: #2980b9;
        margin: 2.5rem 0;
    }
    
    /* Small text helper */
    small, .uploadedFileName {
        font-size: 1.1rem !important;
        color: #333333 !important;
    }
    
    /* Guidelines box */
    .guidelines-box {
        background: linear-gradient(135deg, #fff9e6 0%, #fff3cd 100%);
        border-left: 5px solid #f0ad4e;
        border-radius: 10px;
        padding: 1.5rem 2rem;
        margin: 1.5rem 0 2rem 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
    }
    
    .guidelines-box h3 {
        color: #856404 !important;
        font-size: 1.6rem !important;
        margin-bottom: 1rem !important;
    }
    
    .guidelines-box ol {
        margin-left: 1.5rem;
        color: #5a4a00 !important;
    }
    
    .guidelines-box li {
        font-size: 1.2rem !important;
        color: #5a4a00 !important;
        margin-bottom: 0.8rem;
        line-height: 1.7 !important;
    }
    
    .guidelines-box ul {
        margin-left: 1rem;
        margin-top: 0.5rem;
    }
    
    .guidelines-box ul li {
        font-size: 1.1rem !important;
        margin-bottom: 0.5rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 2px solid #e0e0e0;
        color: #666666 !important;
        font-size: 1.1rem !important;
    }
    
    .footer span {
        color: #666666 !important;
    }
    
    .footer a {
        color: #2980b9 !important;
        text-decoration: none;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- Title --------------------
st.markdown('<h1 class="main-title">🚗 Tyre Data Formatter</h1>', unsafe_allow_html=True)

# -------------------- Guidelines --------------------
st.markdown('''
<div class="guidelines-box">
    <h3>📖 Zaruri Guidelines (Pehle Padh Lo!)</h3>
    <ol>
        <li><strong>Pehle Output Type choose karo</strong> – "Car Radial Tyre RFT" ya "Radial Tubeless RFT" mein se ek select karo.</li>
        <li><strong>Excel ya CSV file upload karo</strong> – Dono chalega! Par ye dhyan rakho:
            <ul>
                <li>Column names sahi hone chahiye: <strong>W, R, RS</strong></li>
                <li>Company column ka title empty nahi hona chahiye – agar empty hai to <strong>"company"</strong> likh do, warna error aayega.</li>
            </ul>
        </li>
        <li><strong>Step 3 mein Preview dekho</strong> – Check karo ki data sahi format mein aa raha hai ya nahi.</li>
        <li><strong>Step 4 mein "Copy to Clipboard" dabao</strong> – Phir seedha Excel mein paste kar do. Done! ✅</li>
    </ol>
</div>
''', unsafe_allow_html=True)

# -------------------- Mode Selection --------------------
st.markdown('<p class="section-header">📋 Step 1: Select Output Type</p>', unsafe_allow_html=True)

mode = st.radio(
    "",
    ["Car Radial Tyre RFT", "Radial Tubeless RFT"],
    horizontal=True
)


# -------------------- Helpers --------------------

def normalize_cols(cols):
    return (
        cols.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "")
    )


def detect_header_row(df_raw):
    required = {"w", "r", "rs", "company"}

    for i in range(len(df_raw)):
        row = normalize_cols(df_raw.iloc[i])
        if required.issubset(set(row)):
            return i
    return None


def clean_numeric(series):
    return pd.to_numeric(series, errors="coerce")


# -------------------- File Upload --------------------
st.markdown("---")
st.markdown('<p class="section-header">📁 Step 2: Upload Your File</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xls", "xlsx"],
    help="Upload your tyre data file here"
)

if uploaded_file:

    try:
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()

        # Read raw without assuming header
        if file_ext == ".csv":
            df_raw = pd.read_csv(uploaded_file, header=None)
        else:
            df_raw = pd.read_excel(uploaded_file, header=None)

        header_row = detect_header_row(df_raw)

        if header_row is None:
            st.error("Could not detect header row containing W, R, RS, Company.")
            st.stop()

        uploaded_file.seek(0)

        if file_ext == ".csv":
            df = pd.read_csv(uploaded_file, header=header_row)
        else:
            df = pd.read_excel(uploaded_file, header=header_row)

        # Normalize columns
        df.columns = normalize_cols(df.columns)

        column_map = {
            "w": ["w", "width"],
            "r": ["r", "ratio", "aspectratio"],
            "rs": ["rs", "rim", "rimsize"],
            "company": ["company", "brand", "manufacturer"]
        }

        resolved = {}

        for key, aliases in column_map.items():
            for col in df.columns:
                if col in aliases:
                    resolved[key] = col
                    break

        if len(resolved) != 4:
            st.error("Required columns not found after header detection.")
            st.stop()

        # -------------------- Data Cleaning --------------------

        df[resolved["w"]] = clean_numeric(df[resolved["w"]])
        df[resolved["r"]] = clean_numeric(df[resolved["r"]])
        df[resolved["rs"]] = clean_numeric(df[resolved["rs"]])

        df = df.dropna(subset=[
            resolved["w"],
            resolved["r"],
            resolved["rs"],
            resolved["company"]
        ])

        df[resolved["w"]] = df[resolved["w"]].astype(int)
        df[resolved["r"]] = df[resolved["r"]].astype(int)
        df[resolved["rs"]] = df[resolved["rs"]].astype(int)

        # -------------------- Format Selection --------------------

        if mode == "Car Radial Tyre RFT":
            suffix = " Car Radial Tyre RFT "
        else:
            suffix = " Radial Tubeless RFT "

        df["Formatted"] = (
            "Tire "
            + df[resolved["w"]].astype(str) + "/"
            + df[resolved["r"]].astype(str)
            + " R"
            + df[resolved["rs"]].astype(str)
            + suffix
            + df[resolved["company"]].astype(str)
        )

        # -------------------- Preview --------------------
        st.markdown("---")
        st.markdown('<p class="section-header">👀 Step 3: Preview Your Data</p>', unsafe_allow_html=True)
        st.success(f"✅ Successfully processed {len(df)} tyre entries!")
        st.dataframe(df[["Formatted"]], use_container_width=True, height=300)

        # -------------------- Copy Output --------------------

        formatted_text = ",\n".join(df["Formatted"]) + ","

        st.markdown("---")
        st.markdown('<p class="section-header">📋 Step 4: Copy or Download</p>', unsafe_allow_html=True)

        components.html(f"""
        <style>
            .output-container {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .output-textarea {{
                width: 100%;
                height: 280px;
                padding: 15px;
                font-size: 1rem;
                line-height: 1.6;
                border: 2px solid #e0e0e0;
                border-radius: 12px;
                background-color: #fafafa;
                resize: vertical;
                color: #333;
            }}
            .output-textarea:focus {{
                outline: none;
                border-color: #3498db;
                box-shadow: 0 0 10px rgba(52, 152, 219, 0.2);
            }}
            .copy-btn {{
                margin-top: 15px;
                padding: 14px 35px;
                font-size: 1.2rem;
                font-weight: 600;
                color: white;
                background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
                border: none;
                border-radius: 10px;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
                transition: all 0.3s ease;
            }}
            .copy-btn:hover {{
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
            }}
            .copy-btn:active {{
                transform: translateY(0);
            }}
            .copy-success {{
                display: none;
                margin-left: 15px;
                padding: 10px 20px;
                background-color: #d4edda;
                color: #155724;
                border-radius: 8px;
                font-size: 1.1rem;
                font-weight: 500;
            }}
        </style>
        <div class="output-container">
            <textarea id="outputbox" class="output-textarea">{formatted_text}</textarea>
            <br>
            <button onclick="copyText()" class="copy-btn">📋 Copy to Clipboard</button>
            <span id="copySuccess" class="copy-success">✓ Copied!</span>
        </div>

        <script>
        function copyText() {{
            var copyText = document.getElementById("outputbox");
            copyText.select();
            copyText.setSelectionRange(0, 99999);
            document.execCommand("copy");
            
            var successMsg = document.getElementById("copySuccess");
            successMsg.style.display = "inline-block";
            setTimeout(function() {{
                successMsg.style.display = "none";
            }}, 2000);
        }}
        </script>
        """, height=420)

        # -------------------- Download --------------------
        st.markdown("")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                "⬇️ Download Output File",
                formatted_text,
                file_name="formatted_output.txt",
                mime="text/plain",
                use_container_width=True
            )

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")

# -------------------- Footer --------------------
st.markdown('''
<div class="footer">
    <span>Made with ❤️ by <strong>Lakshya Bhatnagar</strong></span>
    <span>Contact: <a href="mailto:lakshyabhatnagar1@gmail.com">lakshyabhatnagar1@gmail.com</a></span>
</div>
''', unsafe_allow_html=True)