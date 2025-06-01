import logging
from datetime import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import traceback

# Configura o logger global
logger = logging.getLogger("app-logger")
logger.setLevel(logging.INFO)

# Saída no terminal
console_handler = logging.StreamHandler()
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class GlobalLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.utcnow()
        try:
            response = await call_next(request)
            process_time = (datetime.utcnow() - start_time).total_seconds()

            logger.info(
                f"{request.method} {request.url.path} "
                f"→ {response.status_code} | {request.client.host} | {process_time:.3f}s"
            )
            return response

        except Exception as e:
            tb = traceback.format_exc()
            logger.error(
                f"EXCEPTION → {request.method} {request.url.path} | {request.client.host} | "
                f"{type(e).__name__}: {e}\n{tb}"
            )
            return Response("Internal Server Error", status_code=500)
