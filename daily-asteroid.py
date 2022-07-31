import requests
from datetime import date

today = date.today()
key = 'KIRMxoxN66Ck4kVlOpIc9dBcY9hwHqPNYtRUJeUL'

request = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={today}&api_key={key}')
request.raise_for_status()
data = request.json()

print(f"Number of Near Earth Objects for Today: {len(data['near_earth_objects'][f'{today}'])}\n")

for object in data["near_earth_objects"][f"{today}"]:

    name = object['name']
    is_dangerous = object['is_potentially_hazardous_asteroid']
    diameter_est_meters = object['estimated_diameter']['meters']
    min_diameter_est_meters = object['estimated_diameter']['meters']['estimated_diameter_min']
    max_diameter_est_meters = object['estimated_diameter']['meters']['estimated_diameter_max']

    close_approach_miles = object['close_approach_data'][0]['miss_distance']['miles']
    close_approach_rel_vel_miles = object['close_approach_data'][0]['relative_velocity']['miles_per_hour']

    print(f"Name of Object: {name}\n"
          f"Is Dangerous: {is_dangerous}\n"
          f"Minimum Object Estimate (meters): {min_diameter_est_meters}\n"
          f"Largest Object Estimate (meters): {max_diameter_est_meters}\n"
          f"Object Closest Distance (miles): {close_approach_miles}\n"
          f"Object Speed (miles) During Approach: {close_approach_rel_vel_miles}\n")
