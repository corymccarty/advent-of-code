from collections import namedtuple


Marker = namedtuple("Marker", ["position", "sequence"])


with open("2022/day_6/input.txt") as file:
    stream = file.read()

PACKET_MARKER_SIZE = 4
MESSAGE_MARKER_SIZE = 14


def find_marker(stream: str, marker_size: int) -> Marker | None:
    current_position = marker_size
    while current_position <= len(stream):
        start = current_position - marker_size
        marker_candidate = stream[start:current_position]
        if len(set(marker_candidate)) == marker_size:
            return Marker(current_position, marker_candidate)
        else:
            current_position += 1
    return None


packet_marker = find_marker(stream, PACKET_MARKER_SIZE)
if packet_marker:
    print(
        f"Packet marker {packet_marker.sequence} found at position "
        f"{packet_marker.position}."
    )
else:
    print("Packet marker not found.")

message_marker = find_marker(stream, MESSAGE_MARKER_SIZE)
if message_marker:
    print(
        f"Message marker {message_marker.sequence} found at position "
        f"{message_marker.position}."
    )
else:
    print("Message marker not found.")

print("Finished")
