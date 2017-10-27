import requests

reg = requests.get('https://cars.av.by/search?sort=date&order=desc&year_from=&year_to=2017&currency=USD&price_from=6000&price_to=17000&body_id=&engine_volume_min=&engine_volume_max=&driving_id=&mileage_min=&mileage_max=100000&region_id=&interior_material=&interior_color=&exchange=&search_time=')
print(reg.text)