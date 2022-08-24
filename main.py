import cv2
import base45
import zlib
import cbor2

def decode(filename):

  try:
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

    b45data = data.replace("HC1:", "")
    zlibdata = base45.b45decode(b45data)
    cbordata = zlib.decompress(zlibdata)
    decoded = cbor2.loads(cbordata)
    return cbor2.loads(decoded.value[2])
  except:
    return None