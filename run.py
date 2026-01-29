if __name__ == "__main__":
    import uvicorn
    import os

    # Railway.app provides PORT env variable
    port = int(os.getenv("PORT", 5000))
    
    # Bind to 0.0.0.0 for Railway deployment
    uvicorn.run(
        app="src.main:app",
        host="0.0.0.0",
        port=port,
        reload=False  # Disable reload in production
    )
