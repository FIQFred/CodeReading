def process_csv_file(filename):
    try:
        data = []
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            if line.strip():
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    record = {
                        'name': parts[0],
                        'age': int(parts[1]),
                        'city': parts[2]
                    }
                    data.append(record)
        file.close()
        return data
    except:
        return []

def process_tsv_file(filename):
    try:
        data = []
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            if line.strip():
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    record = {
                        'name': parts[0],
                        'age': int(parts[1]),
                        'city': parts[2]
                    }
                    data.append(record)
        file.close()
        return data
    except:
        return []

def calculate_average_age_csv(filename):
    try:
        total_age = 0
        count = 0
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            if line.strip():
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    total_age += int(parts[1])
                    count += 1
        file.close()
        return total_age / count
    except:
        return 0