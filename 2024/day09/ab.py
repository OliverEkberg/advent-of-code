disk_map = next(open(0)).strip()


def parse_disk_map(split_file_blocks):
    # [block_len, idx, id or '.']
    files = []
    free_spaces = []

    disk_idx = 0
    file_id = 0
    for i, block_len in enumerate(map(int, disk_map)):
        if not block_len:
            continue

        if i % 2:
            free_spaces.append([block_len, disk_idx, '.'])
        else:
            if split_file_blocks:
                files.extend([1, disk_idx + offset, file_id] for offset in range(block_len))
            else:
                files.append([block_len, disk_idx, file_id])

            file_id += 1
        disk_idx += block_len

    return files, free_spaces


def compact_and_compute_checksum(files, free_spaces):
    compacted = []

    for file_size, file_idx, file_id in reversed(files):
        selected_free_space = None

        for i, free_space in enumerate(free_spaces):
            if free_space[1] >= file_idx:
                break
            if free_space[0] >= file_size:
                selected_free_space = free_space
                break

        if not selected_free_space:
            compacted.append([file_size, file_idx, file_id])
            continue

        compacted.append([file_size, selected_free_space[1], file_id])

        selected_free_space[0] -= file_size
        selected_free_space[1] += file_size
        if not selected_free_space[0]:
            free_spaces.pop(i)

    return sum(
        idx * file_id
        for file_size, file_idx, file_id in compacted
        for idx in range(file_idx, file_idx + file_size)
    )


print(compact_and_compute_checksum(*parse_disk_map(split_file_blocks=True)))
print(compact_and_compute_checksum(*parse_disk_map(split_file_blocks=False)))
