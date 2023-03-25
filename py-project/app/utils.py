def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def get_percentage(percentage_dict):
  population_dict = {
   percentage_dict['Country/Territory'] : int(percentage_dict["World Population Percentage"])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def world_population_percentage(data):
  percentage = list(map(lambda item: item["World Population Percentage"], data))
  return percentage

def countrys(data):
  country = list(map(lambda c: c['Country/Territory'], data))
  return country

