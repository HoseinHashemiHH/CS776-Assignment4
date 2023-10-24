def read_tsp_file(file_path):
    cities = []
    reading_coords = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            if reading_coords:
                if line == "EOF":
                    break
                parts = line.split()
                if len(parts) == 3:
                    city_id = int(parts[0])
                    x = float(parts[1])
                    y = float(parts[2])
                    cities.append((x, y))
            elif line.startswith("NODE_COORD_SECTION"):
                reading_coords = True
    return cities

