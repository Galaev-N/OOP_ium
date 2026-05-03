from new_models import *
# ======== Стратегии сортироваки ======== #

class SBP: # Sort By Price
        def __call__(self, product):
            return product.price

class SBN: # Sort By Name
        def __call__(self, product):
            return product.name

class SBI: # Sort By Id
        def __call__(self, product):
            return product.id
#-----------------------------------------#


# ======== Стратегии фильтрации ========  #

class FBQ: # Filter By Quantity
        def __call__(self, product):
            return product.quantity > 0 

class FBM: # Filter By Mark
        def __call__(self, product):
            return product.mark >= 3.0

class FT: # Filter Technic
        def __call__(self, product):
            return not(isinstance(product, Technic))

class FF: # Filter Technic
        def __call__(self, product):
            return not(isinstance(product, Food))

class FE: # Filter Technic
        def __call__(self, product):
            return not(isinstance(product, Estate))
#-----------------------------------------#


# ======== Стратегии трансформации ========  #

class CS: # Change Status
        def __call__(self, product):
            product.status = not(product.status)
            return product

class СС: # Clear Comments
        def __call__(self, product):
            product.comments = {}
            return product
#--------------------------------------------#


# ======== Фабрики ======== #

def Specific_S(attr): 
        def SBA(product):
                if hasattr(product, attr): return  product.attr
                else: return None
        return SBA

def Specific_FP(number=float): # Filter Price
    def filter_fn(product):
        return product.price <= number
    return filter_fn
# ---------------------------#
                        
