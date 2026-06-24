from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database import get_db


app=FastAPI()

class userdata(BaseModel):
    username:str
    password:str 


@app.post("/register")
def RegisterUser(user:userdata):
    try:
        conn=get_db()
        connect=conn.cursor()

        connect.execute("SELECT * FROM UserLogin WHERE UserName=?",(user.username,))
        existing_user = connect.fetchone()

        if existing_user:
            raise HTTPException(status_code=400,detail="Username already exists.Please choose a different one")
        connect.execute("INSERT INTO UserLogin (UserName,Password) VALUES (?,?)", (user.username,user.password))
        
        conn.commit()
        conn.close()

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500,detail="Internal server error")
    
    return {"message":"User Registered Successfully!"}

@app.post("/Login")
def Login(user:userdata):
    try:
        conn=get_db()
        connect=conn.cursor()

        connect.execute("SELECT * FROM UserLogin WHERE UserName=? AND Password=?",(user.username,user.password))
        matched_user=connect.fetchone()
        if matched_user:
            return {"message":"Login Successful"}

        else :
            raise HTTPException(status_code=400,detail="Invalid username or password")
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
