import streamlit as st
from main import decode

st.title("Covid Pass QR decoder")
st.markdown("If you're interested what information your EU digital COVID certificate stores, you can use this little tool to decode it.")

with st.expander("Here's how it works"):
    code = '''    image = cv2.imread(filename)
detector = cv2.QRCodeDetector()
data, _, _ = detector.detectAndDecode(image)

b45data = data.replace("HC1:", "")
zlibdata = base45.b45decode(b45data)
cbordata = zlib.decompress(zlibdata)
decoded = cbor2.loads(cbordata)'''
    st.code(code, language='python')


st.markdown("---")
st.markdown("Upload a foto of your QR-code here to get the information read out.")

uploaded_file = st.file_uploader("Upload a foto or screenshot of your QR-code here")
if uploaded_file is not None:
    print(uploaded_file)

    bytes_data = uploaded_file.getvalue()
    print()
    newname=f"aaa_{uploaded_file.name}"

    with open(newname,"wb") as f:
        f.write(bytes_data)

    result = decode(newname)

    if result is None:
        st.error("Can't read QR code from image.")
    else:
        st.balloons()
        st.markdown("---")
        st.markdown("Here's the results:")
        st.json(result)

