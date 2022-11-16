def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('santiago', 'chile')
print(city)

city = city_country('Abu dhabi', 'UAE')
print(city)

city = city_country('Cairo', 'Egypt')
print(city)