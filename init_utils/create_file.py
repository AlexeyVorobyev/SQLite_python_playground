def create_file(path: str, name: str, ext: str, content: str):
    file = open(path + '\\' + name + ext, "w")
    file.write(content)
    file.close()
