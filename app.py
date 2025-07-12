
# import streamlit as st
# import cv2
# import numpy as np
# from utils.overlay_custom import overlay_image

# st.set_page_config(page_title="Virtual Try-On", layout="centered")
# st.title("🧑‍🎨 Flexible Virtual Try-On")

# # Upload user image
# user_img_file = st.file_uploader("Upload your selfie image", type=["jpg", "jpeg", "png"])
# product_img_file = st.file_uploader("Upload overlay product image (e.g., glasses/lipstick/dress)", type=["jpg", "jpeg", "png"])

# if user_img_file and product_img_file:
#     # Decode user image
#     user_bytes = np.asarray(bytearray(user_img_file.read()), dtype=np.uint8)
#     user_img = cv2.imdecode(user_bytes, 1)

#     # Decode product image (preserve alpha if available)
#     product_bytes = np.asarray(bytearray(product_img_file.read()), dtype=np.uint8)
#     product_img = cv2.imdecode(product_bytes, cv2.IMREAD_UNCHANGED)

#     st.image(user_img, caption="Original Selfie", channels="BGR")
#     st.image(product_img, caption="Uploaded Product", channels="BGR" if product_img.shape[2] == 3 else "BGRA")

#     # Sliders to adjust overlay
#     st.subheader("Adjust Position and Scale of Product")
#     x = st.slider("X Offset", 0, user_img.shape[1], user_img.shape[1] // 2)
#     y = st.slider("Y Offset", 0, user_img.shape[0], user_img.shape[0] // 2)
#     scale = st.slider("Scale (%)", 10, 300, 100)

#     # Overlay image
#     result = overlay_image(user_img, product_img, x, y, scale / 100.0)
#     st.image(result, caption="Try-On Result", channels="BGR")

import streamlit as st
import cv2
import numpy as np
from utils.overlay_custom import overlay_image
from PIL import Image

st.set_page_config(page_title="Virtual Try-On", layout="centered")
st.title("🧑‍🎨 Flexible Virtual Try-On")

# Upload user image
user_img_file = st.file_uploader("Upload your selfie image", type=["jpg", "jpeg", "png"])
product_img_file = st.file_uploader("Upload overlay product image (e.g., glasses/lipstick/dress)", type=["jpg", "jpeg", "png"])

if user_img_file and product_img_file:
    # Decode user image
    user_bytes = np.asarray(bytearray(user_img_file.read()), dtype=np.uint8)
    user_img = cv2.imdecode(user_bytes, 1)

    # Decode product image (preserve alpha if available)
    product_bytes = np.asarray(bytearray(product_img_file.read()), dtype=np.uint8)
    product_img = cv2.imdecode(product_bytes, cv2.IMREAD_UNCHANGED)

    st.image(user_img, caption="Original Selfie", channels="BGR")
    st.image(product_img, caption="Uploaded Product", channels="BGR" if product_img.shape[2] == 3 else "BGRA")

    # Sliders to adjust overlay
    st.subheader("Adjust Position and Scale of Product")
    x = st.slider("X Offset", 0, user_img.shape[1], user_img.shape[1] // 2)
    y = st.slider("Y Offset", 0, user_img.shape[0], user_img.shape[0] // 2)
    scale = st.slider("Scale (%)", 10, 300, 100)

    # Overlay image
    result = overlay_image(user_img, product_img, x, y, scale / 100.0)
    st.image(result, caption="Try-On Result", channels="BGR")

    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    result_pil = Image.fromarray(result_rgb)

# Download button
st.markdown("### 📥 Download Your Try-On Result")
st.download_button(
    label="Download Image",
    data=result_pil.tobytes(),
    file_name="tryon_result.jpg",
    mime="image/jpeg"
)

