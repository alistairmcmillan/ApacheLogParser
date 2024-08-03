import datetime
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

    d = datetime.datetime.now()
    filename_output = (f'report {d.year}{d.month:02d}{d.day:02d}'
                       f'{d.hour:02d}{d.minute:02d}{d.second:02d}.html')
    with open(filename_output, 'w') as f:
        f.write('<html><head>')
        f.write('<style>table { font-size: 10px !important; }</style>')
        f.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">')
        f.write('</head><body>\n')
        f.write('<table class="table" style="margin-left: auto; margin-right: auto; width: 80%">\n')
        f.write('<thead><tr><th>Resource</th><th>Visitor Count</th></tr></thead>\n')
        f.write('<tbody>\n')
        for resource in reversed(sorted(resource_dict.items(), key=operator.itemgetter(1))):
            f.write(f'<td>https://escwiki{resource[0]}</td><td>{resource[1]}</td></tr>\n')
        f.write('</tbody>\n')
        f.write('</table>\n')
        f.write('</body></html>\n')

#    print('\nVISITOR ADDRESSES')
#    for address in reversed(sorted(address_dict.items(), key=operator.itemgetter(1))):
#        print(address)
