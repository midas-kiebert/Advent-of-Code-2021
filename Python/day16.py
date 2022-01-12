hexadecimal = open('inputs/day16.txt').read()

INF = 1e99
binary = ''.join([format(int(digit, 16), '04b') for digit in hexadecimal])
versions_total = 0
def read(search_window):
    global current_index
    ret_val = binary[current_index:current_index+search_window]
    current_index += search_window
    return ret_val

def read_packet(remove_trailing=True):
    global versions_total, current_index
    packet_version = read(3)
    packet_type_ID = int(read(3), 2)
    if packet_version:
        versions_total += int(packet_version, 2)
    number = 0

    if packet_type_ID == 4:
        done = False
        string = ''
        while not done:
            current = read(5)
            if current[0] == '0':
                done = True
            string += current[1:]
        number = int(string, 2)
    elif packet_type_ID == 0:
        number = 0
        length_type_ID = read(1)
        if length_type_ID == '0':
            length = int(read(15), 2)
            max_index = current_index + length
            while current_index < max_index:
                number += read_packet(False)
        else:
            num_of_packets = int(read(11), 2)
            for _ in range(num_of_packets):
                number += read_packet(False)
    elif packet_type_ID == 1:
        number = 1
        length_type_ID = read(1)
        if length_type_ID == '0':
            length = int(read(15), 2)
            max_index = current_index + length
            while current_index < max_index:
                number *= read_packet(False)
        else:
            num_of_packets = int(read(11), 2)
            for _ in range(num_of_packets):
                number *= read_packet(False)
    elif packet_type_ID == 2:
        number = INF
        length_type_ID = read(1)
        if length_type_ID == '0':
            length = int(read(15), 2)
            max_index = current_index + length
            while current_index < max_index:
                number = min(read_packet(False), number)
        else:
            num_of_packets = int(read(11), 2)
            for _ in range(num_of_packets):
                number = min(read_packet(False), number)
    elif packet_type_ID == 3:
        number = 0
        length_type_ID = read(1)
        if length_type_ID == '0':
            length = int(read(15), 2)
            max_index = current_index + length
            while current_index < max_index:
                number = max(read_packet(False), number)
        else:
            num_of_packets = int(read(11), 2)
            for _ in range(num_of_packets):
                number = max(read_packet(False), number)
    elif packet_type_ID == 5:
        if binary[current_index] == '0':
            current_index += 16
        else:
            current_index += 12
        val1 = read_packet(False)
        val2 = read_packet(False)
        number = val1 > val2
    elif packet_type_ID == 6:
        if binary[current_index] == '0':
            current_index += 16
        else:
            current_index += 12
        val1 = read_packet(False)
        val2 = read_packet(False)
        number = val1 < val2
    elif packet_type_ID == 7:
        if binary[current_index] == '0':
            current_index += 16
        else:
            current_index += 12
        val1 = read_packet(False)
        val2 = read_packet(False)
        number = val1 == val2
    if remove_trailing:
        while current_index < len(binary) and binary[current_index] == '0':
            current_index += 1
    return number

current_index = 0
part2 = read_packet()
print(versions_total)
print(part2)
