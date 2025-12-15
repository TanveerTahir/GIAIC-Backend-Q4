from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def students():
    student =[{
        "name": "Tanveer Tahir",
        "age": 24,
        "city": "Karachi"
    },
    {
        "name": "Ali Raza",
        "age": 22,
        "city": "Lahore"
    }]
    return student
