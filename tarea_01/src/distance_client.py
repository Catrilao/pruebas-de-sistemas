import grpc
import distance_unary_pb2_grpc as pb2_grpc
import distance_unary_pb2 as pb2
from google.protobuf.json_format import MessageToJson
import json


def main(source, destination, unit, print_message):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.DistanceServiceStub(channel)

        # a SourceDest contains two Position: source and destination
        message = pb2.SourceDest(
            source=pb2.Position(latitude=source[0], longitude=source[1]),
            destination=pb2.Position(latitude=destination[0], longitude=destination[1]),
            unit=unit,
        )

        if print_message:
            print(f"Message sent:\n{MessageToJson(message)}\n")

        # call remote method
        response = stub.geodesic_distance(message)

        try:
            response = {
                "Distance": json.loads(MessageToJson(response))["distance"],
                "Method": json.loads(MessageToJson(response))["method"],
                "Distance unit": json.loads(MessageToJson(response))["unit"],
            }
        except KeyError:
            response = "One or more key are missing!"

        return response


if __name__ == "__main__":
    response = main(
        source=(81, 30),
        destination=(40, 30),
        unit="",
        print_message=True,
    )

    print(response)
