import cv2

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("Ih, deu erro, não consegui ler sua webcam")

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(width)

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(height)

fps = int(vid.get(cv2.CAP_PROP_FPS))
#print(fps)

out = cv2.VideoWriter("CaraCameraLenta4.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))


while(True):
    ret, frame = vid.read()

    cv2.imshow("Video", frame)
    out.write(frame)
    if cv2.waitKey(1000) == 32:
        break

vid.release()
out.release()
vid.destroyAllWindows()