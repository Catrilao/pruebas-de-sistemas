import requests
import json


def distance(source, destination, unit):
    begin = {
        "geometryType": "esriGeometryPoint",
        "geometry": {
            "x": source[0],
            "y": source[1],
        },
    }

    end = {
        "geometryType": "esriGeometryPoint",
        "geometry": {
            "x": destination[0],
            "y": destination[1],
        },
    }

    if unit == "km" or unit == "":
        unit = "9036"
    elif unit == "nm":
        unit = "9030"

    url = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Utilities/Geometry/GeometryServer/distance"
    params = {
        "sr": 4326,
        "distanceUnit": unit,
        "geometry1": json.dumps(begin),
        "geometry2": json.dumps(end),
        "geodesic": True,
        "f": "json",
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data


if __name__ == "__main__":
    res = distance(
        source=(89, 30),
        destination=(81, 33),
        unit="km",
    )

    print(res)
