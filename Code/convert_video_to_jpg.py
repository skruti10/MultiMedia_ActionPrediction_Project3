import cv2
import os
import getopt
import sys

import constants as c
source = ''

def main():
    ##
    # Handle command line input, generate the video for the selected directory containing a video file.
    ##

    

    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'v:H',
                                ['video_dir=', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-v', '--video_dir'):
            source = c.get_dir(arg)
        if opt in ('-H', '--help'):
            usage()
            sys.exit(2)


    for root, dirs, filenames in os.walk(source):
        for f in filenames:
            print('Reading video file:', f)
            name = str(f).split(".")
            fullpath = os.path.join(source, f)
            vidcap = cv2.VideoCapture(fullpath)
            success,image = vidcap.read()
            count = 0
            success = True
            while success:
                success,image = vidcap.read()
                #print ('Read a new frame: ', success)
                newDir = os.path.join(source,name[0])
                newFileName = name[0] +"_frame"+str(count)+".jpg"
                #print('file name:', newFileName)
                finalFilePath = os.path.join(newDir, newFileName)
                #print('final path:', finalFilePath)
                if not os.path.exists(newDir):
                    print('creating dir:', newDir)
                    os.makedirs(newDir)
                cv2.imwrite(finalFilePath, image)     # save frame as JPEG file
                count += 1


if __name__ == '__main__':
    main()
