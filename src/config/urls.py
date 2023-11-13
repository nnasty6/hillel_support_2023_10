from django.contrib import admin
from django.urls import include, path

from .exchange_rates import exchange_rates, get_information_from_history

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
    # path("api-auth/", include("rest_framework.urls")),
    path("exhange-rates/", exchange_rates),
    path("exchange-rates/history", get_information_from_history)
    # path("users/all", api.all),
    # path("users/create", api.create),
]

# from users import api
# from .exchange_rates import exchange_rates

# def get_message():
#     return {"message": "ok"}

# # REST
# # controller
# def foo(request):
#     # model - бизнес логика
#     data = get_message()
#     response = JsonResponse(data) # JsonResponse is view
#     # controller
#     return response
