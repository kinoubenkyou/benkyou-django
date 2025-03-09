from rest_framework.routers import Route, SimpleRouter


class SingleResourceRouter(SimpleRouter):
    routes = [
        Route(
            url=r"^{prefix}$",
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
    ]
