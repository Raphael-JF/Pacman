import json,os

class JSON_handler():

    def __init__(self,data:dict={}):

        if type(data) is not dict:
            self.read(data)
        else:
            self.data = data


    def save(self,path:list[str]|str):

        if type(path) is not str:
            path = os.path.join(os.getcwd(),'backup_files',*path)
        with open(path,'w',encoding = "utf-8") as f:
                json.dump(self.data,f,ensure_ascii=False)


    def read(self,path:list[str]|str):

        if type(path) is not str:
            path = os.path.join(os.getcwd(),'backup_files',*path)
        with open(path,"r",encoding="utf-8") as f:
            self.data = json.load(f)
            

    def __getitem__(self, key):

        return self.data[key]


    def __setitem__(self, key, value):

        self.data[key] = value


    def __str__(self):

        return json.dumps(self.data)