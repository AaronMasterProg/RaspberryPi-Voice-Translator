import cv2

modelo_clasificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

captura_video = cv2.VideoCapture(0)

def delimitador(vid):
    imagen_gris = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    caras = modelo_clasificador.detectMultiScale(imagen_gris, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in caras:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return caras

def recognition():
    while True:

        resultado, video_frame = captura_video.read()
        if resultado is False:
            break

        caras = delimitador(
            video_frame
        )

        cv2.imshow(
            "Mi cara", video_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    captura_video.release()
    cv2.destroyAllWindows()
