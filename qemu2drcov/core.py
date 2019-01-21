import re
import struct

HEADER = b'DRCOV VERSION: 2\n' \
         b'DRCOV FLAVOR: drcov-64\n' \
         b'Module Table: version 2, count 1\n' \
         b'Columns: id, base, end, entry, path\n'

def parsePages(inLines):
    pagesList = ['start_brk', 'end_code', 'start_code', 'start_data', 'end_data',
             'start_stack', 'brk', 'entry', 'argv_start', 'env_start', 'auxv_start']
    pageDict = {}

    for line in inLines:
        if re.search(r'(Trace|Chain|Linking)', line):
            break

        for page in pagesList:
            regex = re.compile(page + '\s*(0x[0-9a-f]+)')
            r = regex.search(line)
            if r:
                pageDict[page] = r.group(1)

    return pageDict

def parseTraces(inLines):
    tracesList = []

    regex = re.compile(r'Trace\s+[0-9]:\s+0x[0-9a-f]+\s+\[(.*)\]')
    for line in inLines:
        r = regex.search(line)
        if r:
            trace = r.group(1).split('/')
            tracesList.append({'cs_base': int(trace[0], 16),
                               'pc': int(trace[1], 16),
                               'size': int(trace[2], 10),
                               'flags': trace[3]})

    return tracesList

def buildDrcov(name, pages, traces):
    data = HEADER
    data += ('0, %s, %s, %s, %s\n' % (pages['start_code'], pages['end_code'],
        pages['entry'], name)).encode('utf-8')
    data += b'BB Table: %d bbs\n' % len(traces)
    for trace in traces:
        data += (trace['pc'] & 0x00000000ffffffff).to_bytes(4, 'little')
        data += trace['size'].to_bytes(2, 'little')
        data += int(0).to_bytes(2, 'little')
    return data
