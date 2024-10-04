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
        source=(-91, 30),
        destination=(40, 30),
        unit="9036",
    )

    print(res)
