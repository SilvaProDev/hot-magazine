from .blog.apiviews import *
from rest_framework.routers import DefaultRouter
#frm rest_framework import routers

router = DefaultRouter()
#router = routers.DefaultRouter()

router.register('categorie', CategoryViewset)
router.register('Produit', ProduitViewset)
router.register('ContactMessage', ContactMessageViewset)

name_app = "api"
urlpatterns = [

]

urlpatterns+= router.urls