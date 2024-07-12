import streamlit as st
from PIL import Image
import app  # Ensure this is your module that contains the predict_step function

def about():
    st.write("## About")
    st.write("### 🌈 How Deep Learning Works for Image Processing")
    st.write(
        "Deep learning for image processing involves training neural networks on large datasets "
        "to learn features and patterns in images. Convolutional Neural Networks (CNNs) are commonly "
        "used for tasks like image classification, object detection, and image captioning. Pre-trained "
        "models, like Vision Transformer (ViT), can be fine-tuned for specific image processing tasks."
    )

    container = st.container()
    container.write("## Make it Easy to Understand")

    container.write(
        "Imagine you have a picture, like a photo of a cat. To make a caption for this picture, a computer needs to look at the image and understand what's happening.\n\n"
        "Breaking Down the Image: the computer uses a special tool (like a super smart camera) to break down the picture into smaller pieces, kind of like noticing different parts of the cat, the background, and so on.\n\n"
        "Remembering the Important Parts: It then remembers the important features of the image, like the cat's ears, eyes, and tail. This is done using a special type of computer brain called a neural network.\n\n"
        "Understanding Words: The computer also knows a lot about words. It understands what words mean and how they fit together. It has learned this from looking at lots of sentences and captions.\n\n"
        "Putting it Together: Now, it's time to combine its knowledge of the picture and its understanding of words. The computer's brain, which is like a storyteller, starts putting words together to describe the picture.\n\n"
        "Getting Better with Practice: The computer practices a lot by looking at many pictures and their captions. It learns from these examples to become better at creating its own captions.\n\n"
        "Teacher Helping Out: During this learning process, the computer gets some help from a teacher. The teacher tells the computer if its captions are good or not. The computer tries to improve based on this feedback.\n\n"
        "Making Captions on its Own: Finally, when you show the computer a new picture, it uses what it has learned to create a caption on its own. It looks at the features of the picture and thinks of words to describe them, creating a caption for the image."
    )

def developers():
    st.write("## 🌟 Developers")
    st.write("### Meet the Developers")

    st.image(
        "https://media.licdn.com/dms/image/D4D03AQH-xOdK5K2fHg/profile-displayphoto-shrink_200_200/0/1694320992432?e=1709164800&v=beta&t=L2W5BSfYGiIyPU24tOcnzZHh7yGnXA4WQ1bh_Ykf5tQ",
        caption="Developer", use_column_width=True, width=40
    )
    st.write("**Name:** SOURAV KUMAR")
    st.write("**GitHub:** [sourav kumar](https://github.com/singhsourav0)")
    st.write("**LinkedIn:** [Sourav Kumar](https://www.linkedin.com/in/singhsourav0)")

    st.write("### 🚀 Future Updates")
    st.write(
        "Stay tuned for future updates and improvements to the Image Caption Generator! "
        "This project is a stepping stone towards building an Instagram caption generator. "
        "In the future, it will generate captions like poetry in Hinglish and English, "
        "complete with emojis and trending hashtags."
    )

def run_streamlit_app():
    st.set_page_config(layout="wide", page_title="🌈 Image Caption Generator", page_icon="🚀")

    st.write("# 🌈 Generate Caption From Input Image")
    st.write("## 🐶 Try uploading an image to watch it magically generate a caption for you.")
    st.sidebar.write("## Upload and Copy 🌈")

    default_image_path = "image/ro.jpg"
    image = Image.open(default_image_path)
    st.image(image, caption="Default Image", use_column_width=True, width=300)

    container = st.container()
    default_caption = app.predict_step([default_image_path])
    container.write("### Default Image Caption:")
    container.markdown(f" > # {default_caption[0]}")

    my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if my_upload is not None:
        if my_upload.size > 5 * 1024 * 1024:  # 5MB
            st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
        else:
            st.image(my_upload, caption="Uploaded Image", use_column_width=True, width=300)
            container = st.container()
            uploaded_caption = app.predict_step([my_upload])
            container.write("## Uploaded Image Caption:")
            container.markdown(f"> # {uploaded_caption[0]}")

    tabs = st.sidebar.radio("Tabs", ("About", "Developers"))

    if tabs == "About":
        about()
    elif tabs == "Developers":
        developers()

    st.sidebar.image("https://media.giphy.com/media/H7CKd1GO6oiZQo7L5d/giphy.gif", caption="Visualize with a GIF", use_column_width=True)
    st.sidebar.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", caption="Visualize with a GIF", use_column_width=True)

if __name__ == "__main__":
    run_streamlit_app()
