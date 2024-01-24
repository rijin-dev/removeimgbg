import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO


def remove_background(input_img):
    output_img = remove(input_img)
    return output_img


# Convert the image to BytesIO so we can download it
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


st.title("이미지 배경 제거")
st.divider()
st.write("#### :sunglasses: 베르데코 직원만 이용하세요. :sunglasses:")

uploaded_file = st.file_uploader("이미지를 업로드 하세요.", type=["png", "jpg", "jpeg"])


if uploaded_file is not None:
    input_img = Image.open(uploaded_file)
    output_img = remove_background(input_img)
    downloadable_image = convert_image(output_img)
    # 결과 출력
    st.success("이미지 배경 제거가 완료 되었습니다.")
    st.subheader("원본 :smirk:", divider="violet")
    st.image(input_img, caption="원본 이미지", use_column_width=True)

    st.subheader("결과 :stuck_out_tongue:", divider="rainbow")
    st.image(output_img, caption="배경 제거 이미지 ", use_column_width=True)
    st.info("결과 이미지 저장을 원하시면 아래 '다운로드 이미지' 버튼을 클릭하세요.")
    st.download_button(
        label="다운로드 이미지",
        data=downloadable_image,
        file_name="output.png",
        mime="image/png",
    )
