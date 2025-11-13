from fastapi import FastAPI
import uvicorn, caesar, fence

app = FastAPI()

@app.get("/test")
def test():
    return {"msg": "hi from test"}

@app.get("/test/:name")
def saved_user(name: str):
    with open("names.txt", "a") as names:
        names.write(name + "\n")
    return {"msg": "saved user"}

@app.post("/caesar/encrypted")
def caesar_encryption(text: str):
    return {"encrypted_text": caesar.encryption(text)}

@app.post("/caesar/decrypted")
def caesar_decryption(text: str):
    return {"decrypted_text": caesar.decryption(text)}

@app.get("/fence/encrypt")
def fence_fence(text: str):
    return {"encrypted_text": fence.encryption(text)}

@app.post("/fence/decrypt")
def fence_decrypt(text: str):
    return {"encrypted_text": fence.encryption(text)}