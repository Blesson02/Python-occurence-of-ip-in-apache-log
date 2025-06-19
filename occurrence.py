import logparser

# Initialize the counter dictionary
counter = {}

# Read the access log
log = open('access.log','r')
for line in log:
        dict1 = logparser.Parser(line)

        # Skip lines that couldn't be parsed
        if dict1 is None:
            continue

        # Extract required fields
        time = dict1["time"]
        ip = dict1["host"]
        status = dict1["status"]

        # Count number of occurrences by IP
        if ip in counter:
            counter[ip] += 1
        else:
            counter[ip] = 1

# Write results to a file
file = open('occurrence.txt','w')
for ip in counter:
        count = counter[ip]
        result = "{:20} : {:3}\n".format(ip, count)
        file.write(result)
