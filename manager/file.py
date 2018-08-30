from datetime import datetime

def save_file(e,action):
    file_error = open("./manager/error.txt","r")
    content = file_error.readlines()
    file_error.close()
    if content:
        if len(content) < 10:
            info = "\n" + str(datetime.now()) + " - " + action + " - " + str(e)
            content.append(info)
        else:
            info = str(datetime.now()) + " - " + action + " - " + str(e)
            content = []
            content.append(info)
    else:
        info = str(datetime.now()) + " - " + action + " - " + str(e)
        content.append(info)
    save_file_error = open("./manager/error.txt","w")
    save_file_error.writelines(content)
    content = None
    save_file_error.close()  