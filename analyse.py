import operator

address_dict = {}
resource_dict = {}

def parse_line(line):
    address_start = line.find(' ')
    address = line[:address_start]

    timestamp_start = line.find('[') + 1
    timestamp_end = line.find(']')
    timestamp = line[timestamp_start:timestamp_end]

    method_start = line.find('\"') + 1
    method_end = line.find(' ', method_start)
    method = line[method_start:method_end]

    resource_start = method_end + 1
    resource_end = line.find(' ', resource_start)
    resource = line[resource_start:resource_end]

    protocol_start = resource_end + 1
    protocol_end = line.find('\"', protocol_start)
    protocol = line[protocol_start:protocol_end]

    result_start = protocol_end + 2
    result_end = line.find(' ', result_start)
    result = line[result_start:result_end]

    size_start = result_end + 1
    size = line[size_start:]

    return [address,
            timestamp,
            method,
            resource,
            protocol,
            result,
            size]

filename = '../logs/access.2009.log'
with open(filename, 'r', encoding='UTF-8') as file:
    while output := file.readline():
        line_new = parse_line(output.rstrip())
        if line_new[0] not in address_dict:
            address_dict[line_new[0]] = 1
        else:
            current_count = address_dict[line_new[0]]
            address_dict[line_new[0]] = current_count+1

        if line_new[3] not in resource_dict:
            resource_dict[line_new[3]] = 1
        else:
            current_count = resource_dict[line_new[3]]
            resource_dict[line_new[3]] = current_count+1

    print('\nVISITED RESOURCES')
    for resource in reversed(sorted(resource_dict.items(), key=operator.itemgetter(1))):
        print(resource)

    print('\nVISITOR ADDRESSES')
    for address in reversed(sorted(address_dict.items(), key=operator.itemgetter(1))):
        print(address)
