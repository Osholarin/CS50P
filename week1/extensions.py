def find_extensions(filename):
    if filename.find(".gif") != -1:
        print("image/gif")
    elif filename.find(".jpg") != -1:
        print("image/jpeg")
    elif filename.find(".png") != -1:
        print("image/png")
    elif filename.find(".jpeg") != -1:
        print("image/jpeg")
    elif filename.find(".pdf") != -1:
        print("application/pdf")
    elif filename.find(".txt") != -1:
        print("text/plain")
    elif filename.find(".zip") != -1:
        print("application/zip")
    elif filename.upper().find("PDF") != -1:
        print("application/pd")
    else:
        print("application/octet-stream")

file_name = input("Enter a filename and extensions >> ").strip().lower()
find_extensions(file_name)