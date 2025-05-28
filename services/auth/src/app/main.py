from fastapi import FastAPI

app = FastAPI()


@app.get(
    '/api/health',
)
async def health_check():
    return {
        'name': 'Auth',
        'description': 'Auth microservice for Multi-Vendor E-Commerce Platform app',
        'version': '1.0.0',
    }
