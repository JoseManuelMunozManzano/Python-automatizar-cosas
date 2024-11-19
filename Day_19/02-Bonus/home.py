import streamlit as st
# Paquete pillow
# PIL es un tipo y vamos a crear instancias de imágenes PIL de ese tipo.
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
import io

st.title("CAMERA FILTER APP")

# Añadimos un control para arrancar cámara
with st.expander("Start Camera"):
  # Arrancamos la cámara
  camera_image = st.camera_input("Camera")

# Lo que decimos con este if es: Si camera_image es un objeto (es decir, no es None)
# Esto es lo que ocurre al principio, cuando el navegador nos pide permisos para usar la cámara.
# Si no indicamos este if, como todavía no se ha arrancado la cámara, el valor en None
# y nos da un error las sentencias siguientes, de ahí el if.
if camera_image:
    # Creamos la instancia.
    img = Image.open(camera_image)

    # Aplicamos distintos filtros
    filter_options = ["Grayscale", "Blur", "Contour", "Edge Enhance", "Sepia", "Emboss", "Rotate"]
    selected_filter = st.selectbox("Select Filter", filter_options)

    if selected_filter == "Grayscale":
        filtered_img = img.convert("L")
    elif selected_filter == "Blur":
        filtered_img = img.filter(ImageFilter.BLUR)
    elif selected_filter == "Contour":
        filtered_img = img.filter(ImageFilter.CONTOUR)
    elif selected_filter == "Edge Enhance":
        filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)
    elif selected_filter == "Sepia":
        filtered_img = img.convert("L").convert("RGB")
        filtered_img = ImageEnhance.Color(filtered_img).enhance(0.5)
    elif selected_filter == "Emboss":
        filtered_img = img.filter(ImageFilter.EMBOSS)
    elif selected_filter == "Rotate":
        angle = st.slider("Rotate Angle", 0, 360, 90)
        filtered_img = img.rotate(angle)

    # Renderizamos la imagen en la página web.
    st.image(filtered_img)

    # Create a download button
    buffer = io.BytesIO()
    filtered_img.save(buffer, format="JPEG")
    buffer.seek(0)

    st.download_button(
        label="Download Image",
        data=buffer,
        file_name="filtered_image.jpg",
        mime="image/jpeg"
    )
