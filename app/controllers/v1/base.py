from fastapi import APIRouter


def new_router(dependencies=None):
    router = APIRouter()
    router.tags = ["V1"]
    # Caddy 在 v.elesos.cc 上通过 `handle_path /api/*` 转发前会剥离外部 "/api" 前缀，
    # 并通过 --root-path "/api" 告知 FastAPI 该外部前缀（用于生成 OpenAPI/Swagger 链接）。
    # 因此这里内部路由前缀只需 "/v1"，避免与外部 "/api" 叠加成 "/api/api/v1/..."。
    router.prefix = "/v1"
    # 将认证依赖项应用于所有路由
    if dependencies:
        router.dependencies = dependencies
    return router
