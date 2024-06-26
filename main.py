from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Memo(BaseModel):
    id:str
    content:str
    
memos=[]

app= FastAPI()
# Create
@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return "ok"    

#Read
@app.get('/memos')
def  read_memo():
    return memos

#Update
@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id==req_memo.id:
            memo.content=req_memo.content
            return "succes"
    return "fail"
            
#Delete
@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
       for index,memo in enumerate(memos):
          if memo.id==memo_id:
              memos.pop(index)
              return "succes"
          return "fail"  

app.mount("/", StaticFiles(directory="static", html=True), name="static")

