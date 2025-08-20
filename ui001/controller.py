import azure.functions as func
from fastapi import APIRouter
from configs.env import get_settings
from utils.application import get_app
from utils.response import response_success

settings = get_settings()

app = get_app()

route_str: str = f"/{settings.api_prefix}/ui001"
healthcheck_router = APIRouter(prefix=route_str, tags=["Healthcheck"])


@healthcheck_router.get("/")
def health_check():    
    return response_success("Health check is good")




async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    app.include_router(healthcheck_router)
    return await func.AsgiMiddleware(app).handle_async(req, context)
