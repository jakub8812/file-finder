import os
#import shutil

i = 1
destination = "/volume1/marketing/+ MISTERO MILANO +/prywatny_folder_jakub/"

lost_items = []
ok_items = []

with open("data.txt", "r") as data:
    data = data.read()


    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for filename in [f for f in filenames if f.endswith(".jpg")]:
            if filename in data:
                if filename not in ok_items:
                    source_file = str(dirpath + "/" + filename)
                    try:
                        # shutil.copy(source_file, destination)
                        print(i, "Poprawnie skopiowano {0} do {1}".format(source_file, destination))
                        ok_items.append(filename)
                        i = i + 1
                    except:
                        pass



with open("data.txt", "r") as data:
    data = data.read()
    data = data.split()

    for line in data:
        if line not in ok_items:
            lost_items.append(line)

    p = 1
    for el in lost_items:
        print(p, el)
        p = p + 1