import cv2

# video to get frames from (put in file path)
capture = cv2.VideoCapture()

totalframecount= int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

totalFrames = 0
framesWanted = 500

frameNr = 0


# intervals for number of frames wante
divider = totalframecount // framesWanted

while (True):
    success, frame = capture.read()

    # break if we finish the video or get the number of frames wanted
    if not success or totalFrames > framesWanted - 1:
        break
    
    if frameNr % divider == 0:
        totalFrames += 1
        cv2.imwrite(f'Frames/frame_{frameNr}.jpg', frame)

    frameNr += 1

capture.release()