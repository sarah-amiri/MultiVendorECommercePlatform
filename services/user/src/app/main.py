from fastapi import FastAPI

app = FastAPI()


@app.get(
    '/api/health',
)
async def health_check():
    return {
        'name': 'User',
        'description': 'User microservice for Multi-Vendor E-Commerce Platform app',
        'version': '1.0.0',
    }
