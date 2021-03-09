source_str = 'Революция!'
target_str = '-'.join(
    [
        source_str[:4] + source_str[-4:],
        source_str[:3] * 4,
        source_str[::-1] * 2,
        source_str[:3] + source_str[4:9:2],
        source_str[-3:] + source_str[1:6:2],
        source_str[:2] + source_str[:-6:-1],
        source_str[9:2:-2] + source_str[2:5:2],
        source_str[6::-2],
        source_str[-7::2]
    ]
)

print(target_str)
