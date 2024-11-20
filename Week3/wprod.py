from fastapi import FastAPI, status, HTTPException
from lprod import Logic 

app = FastAPI()
@app.get("/{a}",status_code= status.HTTP_200_OK)
async def root(a,b):
    z = Logic()
    if int(a)==0 or int(b)==0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="message Failed"
        )
        # return {"message": "Failed"}
    else:
        result = z.multi_num(int(a),int(b))
        return {"message": "Success", "result": result}