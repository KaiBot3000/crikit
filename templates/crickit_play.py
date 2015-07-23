temp = float(raw_input('temperature in F?  '))
chirps_per_minute = 40 + 4 * (temp - 50)
print chirps_per_minute
chirp_time = 60000 / chirps_per_minute
print chirp_time