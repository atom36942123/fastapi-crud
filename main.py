#fastapi app
from fastapi import FastAPI
app=FastAPI()


#root
from fastapi import Request
@app.get("/")
async def root(request:Request):
   response={"hello world"}
   return response


#create
from fastapi import Request
todo=[]
@app.post("/create-todo/{task}")
async def create_todo(request:Request,task:str):
   new_task=[task,"pending"]
   todo.append(new_task)
   response=todo
   return response

#update
from fastapi import Request
@app.put("/update-todo-complete/{id}")
async def update_todo_complete(request:Request,id:int):
   todo[id][1]="completed"
   response=todo[id]
   return response

   
#read single todo by id
from fastapi import Request
@app.get("/read-todo-single/{id}")
async def read_todo_single(request:Request,id:int):
   response=todo[id]
   return response



#read todo
from fastapi import Request
from typing import Optional
@app.get("/all")
async def read_all(request:Request,includeCompleted:Optional[str]=None):
   response=[]
   for item in todo:
      if item[1]=="pending":
         response.append(item)
   #if completed is true
   if includeCompleted=="true":
      response=todo
   #final response
   return response

