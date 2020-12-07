#!/usr/bin/env python3


FILE_BLOCKS = 2000
ENTRY_SIZE_BYTES = 4
ENTRIES_PER_BLOCK = 15


def find_index_blocks():
    remaining = FILE_BLOCKS
    level = "within inode"
    num_index_blocks = 0

    while remaining > 0:

        if level == "within inode":
            num_index_blocks += 1  # this is the inode itself
            remaining -= 12  # the direct block pointers
            level = "single indirect"

        elif level == "single indirect":
            num_index_blocks += 1
            remaining -= ENTRIES_PER_BLOCK
            level = "double indirect"

        elif level == "double indirect":
            num_index_blocks += 1

            remaining_directs = ENTRIES_PER_BLOCK
            while remaining_directs > 0:

                remaining_directs -= 1
                num_index_blocks += 1
                remaining -= ENTRIES_PER_BLOCK

                if remaining <= 0:
                    return num_index_blocks
            level = "triple indirect"

        elif level == "triple indirect":
            num_index_blocks += 1

            remaining_indirects = ENTRIES_PER_BLOCK
            while remaining_indirects > 0:

                num_index_blocks += 1
                remaining_indirects -= 1
                remaining_directs = ENTRIES_PER_BLOCK

                while remaining_directs > 0:

                    remaining_directs -= 1
                    num_index_blocks += 1
                    remaining -= ENTRIES_PER_BLOCK

                    if remaining <= 0:
                        return num_index_blocks

    return num_index_blocks


def find_total_bytes():
    return find_index_blocks() * ENTRY_SIZE_BYTES * ENTRIES_PER_BLOCK


def num_searches():
    """Basically you count "nodes" & "edges" in shortest path to the file block pointer"""

    # If small file (all block pointers in inode)
    if 0 <= FILE_BLOCKS <= 12:
        return 1

    # Single indirect:
    if 13 <= FILE_BLOCKS <= 27:
        return 3

    # Double indirect:
    if 28 <= FILE_BLOCKS <= 225:
        return 5

    # Triple indirect:
    if 226 <= FILE_BLOCKS <= float("inf"):
        return 7


if __name__ == "__main__":
    print("Total bytes =", find_total_bytes(), "\nIndex blocks =", find_index_blocks(), "\nRequired searches =", num_searches())
