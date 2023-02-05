import streamlit as st
from PIL import Image, ImageFilter
import skimage
import matplotlib.pyplot as plt

st.set_page_config(page_title="Basic Image Editor!", page_icon=":pencil:")

# header
st.title("Basic Image Editor :sparkles:")

# sidebar with filter options
with st.sidebar:
    st.header("Filters:")
    image_filter = st.radio("Select Filters here:", ('None (Default)','Greyscale', 'Rainbow Noise (Grainy texture)', 'Blur'))

# image uploader
uploaded_image = st.file_uploader("Upload your image here", type=['jpg','png','jpeg'])

if uploaded_image:
    edited_image = Image.open(uploaded_image)

    # applying filters 
    if image_filter == 'Greyscale':
        edited_image = edited_image.convert("L")

    elif image_filter == 'Blur': 
        intensity = st.slider("Blur intensity:", 1, 10, 3)
        edited_image = edited_image.filter(ImageFilter.GaussianBlur(intensity))

    elif image_filter == 'Rainbow Noise (Grainy texture)':
        # NOTE: rainbow noise code influenced by: https://gist.github.com/Prasad9/28f6a2df8e8d463c6ddd040f4f6a028a?permalink_comment_id=2933012#gistcomment-2933012
        edited_image = skimage.io.imread(uploaded_image)/255.0
        plt.subplot(4, 3, 2)
        grainy_img = skimage.util.random_noise(edited_image, mode="localvar")
        edited_image = grainy_img

    # view before and after
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("before")
        before_image = st.image(uploaded_image)
    
    with col2: 
        st.subheader("after")
        st.image(edited_image)


# note edit css so this is a footer
st.caption("Created by [Tasnim Begom](https://github.com/tasnmb) :frog:")