import uvicorn

if __name__ == "__main__":
    print("Starting Elderly Care Management System (ECMS) Backend...")
    print("API Documentation available at: http://127.0.0.1:8000/docs")
    print("Alternative Redoc at: http://127.0.0.1:8000/redoc")
    print("WebSocket Emergency Channel: ws://127.0.0.1:8000/ws/emergency")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
