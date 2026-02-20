import sys

sys.path.append(r"/Users/galaevka/python_labs-3/src/lab08")
from model import *

milk = product('Молоко 0.5 литров 3.2% жира', 217, 400, 'Простаквашино', 106.3, '#000001', 'Молоко Простаквашино, ручной работы, лично корову доил', {})
cookie = product('Печенье с шоколадом', 120, 1384, 'Юбилейное', 98.5, '#000002', 'Печенько юбилейное, откусанное, Хэмингуэй бы расплакался', {})

print(milk == cookie)
print(milk.info)
print(cookie)
