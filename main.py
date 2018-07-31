import cv2
import Face_Analyze as fa

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        color = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
        cv2.imshow('Press P to take a picture and do a analyze for your face', color)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            cv2.imwrite("test.jpg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    try:
        string = fa.face_analyze("test.jpg")
        print(fa.detail_format(string))
        fa.generateHTML(string)
    except BaseException:
        print("人脸识别出错,可能未检测到人脸或者达到API的QPS上限!")