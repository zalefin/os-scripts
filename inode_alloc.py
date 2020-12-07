#!/usr/bin/env python3


FILE_BLOCKS = 2000
ENTRY_SIZE_BYTES = 4
ENTRIES_PER_BLOCK = 15

DIRECT_IN_INODE = 12


def find_index_blocks():
    """This assumes all index blocks are 15 (12 + 3 for inode, and 15 for indirect and direct blocks),
    if they aren't you'll have to change this function and the find_total_bytes function"""

    remaining = FILE_BLOCKS
    level = "within inode"
    num_index_blocks = 0

    while remaining > 0:

        if level == "within inode":
            num_index_blocks += 1  # this is the inode itself
            remaining -= DIRECT_IN_INODE  # the direct block pointers
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
    """This will have to be something different if not all blocks are 15"""
    return find_index_blocks() * ENTRY_SIZE_BYTES * ENTRIES_PER_BLOCK


def num_searches():
    """Basically you count "nodes" + "edges" in shortest path to the file block pointer"""

    # If small file (all block pointers in inode)
    if 0 <= FILE_BLOCKS <= DIRECT_IN_INODE:
        return 1

    # Single indirect:
    if DIRECT_IN_INODE < FILE_BLOCKS <= (DIRECT_IN_INODE + ENTRIES_PER_BLOCK):
        return 3

    # Double indirect:
    if (DIRECT_IN_INODE + ENTRIES_PER_BLOCK) < FILE_BLOCKS <= ((DIRECT_IN_INODE + ENTRIES_PER_BLOCK) + ENTRIES_PER_BLOCK ** 2):
        return 5

    # Triple indirect:
    if ((DIRECT_IN_INODE + ENTRIES_PER_BLOCK) + ENTRIES_PER_BLOCK ** 2) < FILE_BLOCKS <= float("inf"):
        return 7

    return "Should never get this string"


if __name__ == "__main__":
    print("Total bytes =", find_total_bytes(), "\nIndex blocks =", find_index_blocks(), "\nRequired searches =", num_searches())
