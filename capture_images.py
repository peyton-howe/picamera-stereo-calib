from picamera2 import Picamera2, Preview
from datetime import datetime
from pynput.keyboard import Key, Listener
from libcamera import controls

def show(key):
    
    if key == Key.space:
        now = datetime.now().strftime("%H%M%S")

        picam2a.capture_file("Cam1_frame_{}.jpg".format(now))
        picam2b.capture_file("Cam2_frame_{}.jpg".format(now))
    elif key == Key.esc:
        # Stop listener
        return False

def capture_images():
    with Listener(on_press = show) as listener:  
        listener.join()

    picam2a.stop()
    picam2b.stop()

if __name__ == "__main__":
    if len(Picamera2.global_camera_info()) <= 1:
        print("SKIPPED (one camera)")
        quit()

    picam2a = Picamera2(0)
    picam2a.configure(picam2a.create_preview_configuration())
    picam2a.start_preview(Preview.QTGL)

    picam2b = Picamera2(1)
    picam2b.configure(picam2b.create_preview_configuration())
    picam2b.start_preview(Preview.QT)

    picam2a.start()
    picam2b.start()

    picam2a.set_controls({'AfMode': controls.AfModeEnum.Continuous})
    picam2b.set_controls({'AfMode': controls.AfModeEnum.Continuous})

    #time.sleep(2)
    #print(picam2a.capture_metadata())
    #time.sleep(2)
    #print(picam2b.capture_metadata())
    #picam2a.capture_file("testa.jpg")
    #picam2b.capture_file("testb.jpg")

    capture_images()
