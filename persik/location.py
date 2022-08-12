import requests
import folium


def find_the_location(ip_address):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip_address}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        area = folium.Map(location=[response.get('lat'), response.get('lon')],
                          zoom_start=12)
        folium.CircleMarker(location=(response.get('lat'), response.get('lon')),
                            radius=50).add_to(area)
        name_page = f'persik/{response.get("query")}_{response.get("city")}.html'
        path_page = f'persik/templates/{name_page}'
        area.save(path_page)

    except (requests.exceptions.ConnectionError, ValueError):
        return None
    return name_page





