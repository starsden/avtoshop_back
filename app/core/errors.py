from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def error_response(status_code: int, code: str, message: str, details=None) -> JSONResponse:
    payload = {"error": {"code": code, "message": message}}
    if details is not None:
        payload["error"]["details"] = details
    return JSONResponse(status_code=status_code, content=payload)


async def validation_exception_handler(_: Request, exc: RequestValidationError):
    return error_response(
        status_code=422,
        code="validation_error",
        message="Request validation failed",
        details=exc.errors(),
    )


async def http_exception_handler(_: Request, exc: StarletteHTTPException):
    if isinstance(exc.detail, dict) and "error" in exc.detail:
        return JSONResponse(status_code=exc.status_code, content=exc.detail)
    return error_response(
        status_code=exc.status_code,
        code="http_error",
        message=str(exc.detail),
    )


async def unhandled_exception_handler(_: Request, __: Exception):
    return error_response(
        status_code=500,
        code="internal_server_error",
        message="An unexpected server error occurred",
    )
