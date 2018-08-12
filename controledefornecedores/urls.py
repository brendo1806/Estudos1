from .views import (ControleListView, ControleCreateView, ControleDetailView,
                    ControleUpdateView, ControleDeleteView, home, cadastro, handler404, handler500)
from django.urls import path, include
from .apps import ControledefornecedoresConfig

app_name = ControledefornecedoresConfig.name
urlpatterns = [
    path('controle', ControleListView.as_view(), name='list'),
    path('add/', ControleCreateView.as_view(), name='add'),
    path('<int:pk>/detail/', ControleDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ControleUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ControleDeleteView.as_view(), name='delete'),
    path('', home,),
    path('cadastrodefornecedores.html', cadastro,),
]

handler404 = handler404
handler500 = handler500