import fastapi

from . import restaurant, menu

router = fastapi.APIRouter()
router.include_router(restaurant.router, prefix="/restaurant", tags=["restaurant"])
router.include_router(menu.router, prefix="/menu", tags=["menu"])
