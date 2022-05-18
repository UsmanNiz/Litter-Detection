import cv2
import os

# cap = cv2.VideoCapture("LITTER/VID20220320142848.mp4")
print("Sdfsdfsd")
pathToListDirectory = ("LITTER/")
directoryToSaveFrame = ("Data")


class Directory:
    def __init__(self):
        self.currentDirectory = os.getcwd()
        print("THE CURRENT DIRECTORY ",self.currentDirectory)
        # self.directoryName = directoryName
    # def

    def checkDirectory(self,directoryName):
        pathToCheckNewDir = os.path.join(self.currentDirectory , directoryName)
        return os.path.exists(pathToCheckNewDir)

    def makeDirectory(self,directoryName):
        pathToCreateNewDirectory = os.path.join(self.currentDirectory,directoryName)
        # if not os.path.exists(pathToCreateNewDirectory):
        if not self.checkDirectory(directoryName):
            os.mkdir(pathToCreateNewDirectory)
            print("Directory Created")
            # self.currentDirectory = pathToCreateNewDirectory

    def listDirectory(self,path):
        return os.listdir(path)


class boomboom:
    def __init__(self):
        self.counter = 0

    def showVideo(self,videoPath):
        videoPath = "LITTER/" + videoPath
        cap = cv2.VideoCapture(videoPath)
        print(videoPath)
        while True:
            self.counter = self.counter + 1
            success, frame = cap.read()
            if self.counter % 5 == 0 and success:
                cv2.imshow("Video", frame)
                cv2.waitKey(1000)
            if not success:
                self.counter=0
                break

    def playingMultipleVideos(self,listOfVideos):
        for videoPath in listOfVideos:
            self.showVideo(videoPath)

    def frameWrite(self,videoName, directoryToSaveFrame):
        videoPath = "LITTER/" + videoName
        cap = cv2.VideoCapture(videoPath)
        while True:
            self.counter = self.counter + 1
            success, frame = cap.read()
            if self.counter % 4 == 0 and success:
                frameName = (videoName.split(".")[0]) + str("#") + str(self.counter / 4).split(".")[0] + str(".jpg")
                cv2.imwrite(directoryToSaveFrame + "/" + frameName, frame)
            if not success:
                self.counter = 0
                break
    def frameExtractionFromMultipleVideos(self,listOfVideos):
        for videoPath in listOfVideos:
            self.frameWrite(videoPath, directoryToSaveFrame)


dirObject = Directory()

listOfVideos = dirObject.listDirectory(pathToListDirectory)
dirObject.makeDirectory(directoryToSaveFrame)

blow = boomboom()
blow.frameExtractionFromMultipleVideos(listOfVideos)



# listOfVideos = os.listdir("LITTER/")
# # print(videosList)
# counter = 0
#
# dataDirectory = "Data"
# currentDirectory = os.getcwd()
#
# pathToStoreFrame = os.path.join(currentDirectory, dataDirectory)
#
# isDir = os.path.isdir(dataDirectory)
# if not isDir:
#     os.mkdir(pathToStoreFrame)

# for video in videosList:
#     print(video)
# for video in listOfVideos:
#     # break
#     path = ("LITTER/" + video)
#     cap = cv2.VideoCapture(path)
#     while True:
#         counter = counter + 1
#         success, frame = cap.read()
#         # print(success)
#         if counter % 10 == 0 and success:
#             frameName = (video.split(".")[0]) + str("#") + str(counter/10).split(".")[0] +str(".jpg")
#             print(frameName)
#             cv2.imshow("video" , frame)
#             cv2.imwrite(directoryToSaveFrame +"/"+ frameName,frame)
#             cv2.waitKey(1000)
#         if not success:
#             break
#
#     counter= 0
#
# print("libray imported")