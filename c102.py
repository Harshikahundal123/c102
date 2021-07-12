import cv2
import time
import random
import dropbox
start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        #cv2.imwrite method is used to save an image to any storage device
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token = 'n3B8DUQFRioAAAAAAAAAAflm1YJSrC0_bYqlQJ-sxdY6bSES2r5ZM8PSC-49OMhL'
    file = img_name
    file_from = file
    file_to = "/newFolder1"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.file_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = take_snapshot()
            upload_file(name)
main()

    
