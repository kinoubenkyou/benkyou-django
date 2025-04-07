from rest_framework.routers import DynamicRoute, Route, SimpleRouter


class SingleResourceRouter(SimpleRouter):
    routes = [
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={
                "delete": "destroy",
                "get": "retrieve",
                "patch": "partial_update",
                "post": "create",
                "put": "update",
            },
            name="{basename}",
            detail=False,
            initkwargs={},
        ),
        DynamicRoute(
            url=r"^{prefix}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=False,
            initkwargs={},
        ),
    ]
