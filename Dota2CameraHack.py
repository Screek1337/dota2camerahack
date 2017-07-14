import fileinput, string, sys


def replaceLineInFile(fileName, sourceText, replaceText):
    file = open(fileName, "rb")
    text = file.read()
    file.close()
    file = open(fileName, "wb")
    file.write(text.replace(sourceText, replaceText))
    file.close()
    print("All went well, the modifications are done")


new_camera_distance_value = bytes(input("Enter new camera distance value:"), encoding="ascii")
replaceLineInFile("client.dll", b'1134', new_camera_distance_value)


