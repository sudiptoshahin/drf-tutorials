from django.db import models
from django.utils.translation import gettext_lazy as _


class StockStatus(models.TextChoices):
    IN_STOCK = "IN", _("In Stock")
    OUT_OF_STOCK = "OOS", _("Out Of Stock")
    BO = "BO", _("Back Ordered")

# class model_settings:
    
#     STOCK_STATUS = {
#         "IS": "In Stock",
#         "OOS": "Out Of Stock",
#         "BO": "Back Ordered"
#     }
#     # STOCK_STATUS = (
#     #     ('in_stock', 'In Stock'),
#     #     ('out_of_stock', 'Out of Stock'),
#     #     ('pre_order', 'Pre-order'),
#     # )
    
#     class StockStatus(models.TextChoices):
#         IN_STOCK = "IN", _("In Stock")
#         OUT_OF_STOCK = "OOS", _("Out Of Stock")
#         BO = "BO", _("Back Ordered")
        