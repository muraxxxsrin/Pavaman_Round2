import streamlit as st

# Page setup
st.set_page_config(page_title="Agri Analyzer", layout="wide")
st.title("🌾 Agri Field Analyzer")
st.markdown("Upload `.tiff` files for NDVI or NDRE-based crop analysis. Logic to be added later.")
st.markdown("---")

# Select Task
mode = st.radio("Select Analysis Type", ["🌿 Health Classification (NDVI - 4 Bands)", "🌱 Growth Stage Estimation (NDRE - 8 Bands)"])

# NDVI Mode: 4 separate uploads
if mode == "🌿 Health Classification (NDVI - 4 Bands)":
    st.subheader("🩺 NDVI-Based Health Classification")

    st.markdown("""
    ✅ Upload **4 single-band `.tiff` files**:
    - Red
    - Green
    - NIR
    - Red Edge
    """)

    H_MS_R = st.file_uploader("Upload Red Band", type=["tif", "tiff"], key="ndvi_r")
    H_MS_G = st.file_uploader("Upload Green Band", type=["tif", "tiff"], key="ndvi_g")
    H_MS_NIR = st.file_uploader("Upload NIR Band", type=["tif", "tiff"], key="ndvi_nir")
    H_MS_RE = st.file_uploader("Upload Red Edge Band", type=["tif", "tiff"], key="ndvi_re")

    if all([H_MS_R, H_MS_G, H_MS_NIR, H_MS_RE]):
        st.success("✅ All 4 NDVI bands uploaded successfully!")
        st.info("NDVI calculation and health classification will appear here.")
    else:
        st.warning("📂 Please upload all 4 required bands.")

# NDRE Mode: 4 + 4 uploads
elif mode == "🌱 Growth Stage Estimation (NDRE - 8 Bands)":
    st.subheader("📈 NDRE-Based Growth Stage Estimation")

    st.markdown("""
    ✅ Upload **two sets of 4 `.tiff` files**, representing 8 bands:
    - First 4: Red, Green, NIR, Red Edge
    - Next 4: Remaining spectral bands
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📥 Step 1: Upload First 4 Bands")
        P1_MS_R = st.file_uploader("Upload Red Band", type=["tif", "tiff"], key="ndre1_r")
        P1_MS_G = st.file_uploader("Upload Green Band", type=["tif", "tiff"], key="ndre1_g")
        P1_MS_NIR = st.file_uploader("Upload NIR Band", type=["tif", "tiff"], key="ndre1_nir")
        P1_MS_RE = st.file_uploader("Upload Red Edge Band", type=["tif", "tiff"], key="ndre1_re")

    with col2:
        st.markdown("### 📥 Step 2: Upload Next 4 Bands")
        P2_MS_B5 = st.file_uploader("Upload Band 5", type=["tif", "tiff"], key="ndre2_b5")
        P2_MS_B6 = st.file_uploader("Upload Band 6", type=["tif", "tiff"], key="ndre2_b6")
        P2_MS_B7 = st.file_uploader("Upload Band 7", type=["tif", "tiff"], key="ndre2_b7")
        P2_MS_B8 = st.file_uploader("Upload Band 8", type=["tif", "tiff"], key="ndre2_b8")

    if all([P1_MS_R, P1_MS_G, P1_MS_NIR, P1_MS_RE, P2_MS_B5, P2_MS_B6, P2_MS_B7, P2_MS_B8]):
        st.success("✅ All 8 NDRE bands uploaded successfully!")
        st.info("NDRE calculation and growth stage prediction will appear here.")
    else:
        st.warning("📂 Please upload all 8 required bands.")

# Footer
st.markdown("---")
st.caption("🛠️ UI prototype. Image processing logic will be integrated soon.")
