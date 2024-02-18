import fastapi

from . import restaurant, menu, user

router = fastapi.APIRouter()
router.include_router(restaurant.router, prefix="/restaurant", tags=["restaurant"])
router.include_router(menu.router, prefix="/menu", tags=["menu"])
router.include_router(user.router, prefix="/user", tags=["user"])
