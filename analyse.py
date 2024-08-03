import operator

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

    if result == '200':
        return resource
    else:
        return ''

filename = '../logs/access.2009.log'
with open(filename, 'r', encoding='UTF-8') as file:
    while output := file.readline():
        resource_new = parse_line(output.rstrip())
        if resource_new not in resource_dict:
            resource_dict[resource_new] = 1
        else:
            current_count = resource_dict[resource_new]
            resource_dict[resource_new] = current_count+1

    for resource in sorted(resource_dict.items(), key=operator.itemgetter(1)):
        print(resource)
