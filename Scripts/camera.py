import cv2

def open_camera():
    # Open the camera
    camera = cv2.VideoCapture(0)

    while True:
        # Read the frame from the camera
        ret, frame = camera.read()

        # Display the frame
        cv2.imshow('Camera', frame)

        # Exit the program if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    open_camera()