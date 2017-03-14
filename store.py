import os

def  create_Folder_website(direction):
    if not os.path.exists(direction):
        os.mkdir(direction)
def create_data_files(project_name,url):
    pathlinks=os.path.join( project_name,"linksofwebsite.txt")
    pathcrawled=os.path.join(project_name,"linkscrawled.txt")
    if not os.path.isfile(pathlinks):
        with open(pathlinks, 'w') as p:
            p.write(url)
    if not os.path.isfile(pathcrawled):
        with open(pathcrawled , 'w') as p:
            p.write('')

def add_to_file(direction , data):
    with open(direction ,'a') as f:
        f.writelines(data)
def delete_data(direction):
    open(direction,'w').close()
def file_to_set(direction):
    res = []
    with open(direction,'r') as f:
          for line in f:
              res.append(line)
    return  res
def set_to_file(direction,data):
    with open(direction,'w') as f:
        for val in data:
            f.writelines(val+'\n')
