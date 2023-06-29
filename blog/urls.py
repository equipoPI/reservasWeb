from django.urls import path, include
from rest_framework import routers
from blog import views 

router=routers.DefaultRouter()
router.register(r'User',views.UsuarioViewSet),
router.register(r'Res',views.ReservasViewSet)
router.register(r'Her',views.HerramientasViewSet)
router.register(r'Aul',views.AulaViewSet)
router.register(r'Lab',views.LaboratorioViewSet)

urlpatterns=[
    path('', include(router.urls))
]