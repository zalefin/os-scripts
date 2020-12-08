#!/usr/bin/env python3


FILE_BLOCKS = 2000
ENTRY_SIZE_BYTES = 4
SLOTS_PER_TABLE = 15

DIRECT_IN_INODE = 12


def find_index_blocks(n_blocks):
    """This assumes all index blocks are 15 (12 + 3 for inode, and 15 for indirect and direct blocks),
    if they aren't you'll have to change this function and the find_total_bytes function"""

    remaining = n_blocks
    level = "within inode"
    tables = []

    while remaining_file_blocks > 0:

        if level == "within inode":
            tables.append("inode")  # this is the inode itself

            remaining_file_blocks -= DIRECT_IN_INODE  # the direct block pointers in the inode

            # Advance to next level
            level = "single indirect"

        elif level == "single indirect":

            # Create a direct pointer table and fill its entries with direct pointers to file blocks
            tables.append("direct"); remaining_file_blocks -= SLOTS_PER_TABLE

            # Advance to next level
            level = "double indirect"

        elif level == "double indirect":

            # The double indirect table itself
            tables.append("double indirect")

            # While there are remaining "single indirect slots" in the "double indirect table"
            indirect_slots = SLOTS_PER_TABLE
            while indirect_slots > 0:
                indirect_slots -= 1

                # Create a direct pointer table and fill its entries with direct pointers to file blocks
                tables.append("direct"); remaining_file_blocks -= SLOTS_PER_TABLE

                # Always check if most recently added direct pointer table was enough to satisfy all file blocks
                if remaining_file_blocks <= 0:
                    return len(tables)

            # Advance to next level
            level = "triple indirect"

        elif level == "triple indirect":

            # The triple indirect table itself
            tables.append("triple indirect")

            # While there are remaining "double indirect slots" in the "triple indirect table"
            double_indirect_slots = SLOTS_PER_TABLE
            while double_indirect_slots > 0:
                double_indirect_slots -= 1

                # Allocate a double indirect table
                tables.append("double indirect")

                # While there are remaining "single indirect slots" in this particular "double indirect table"
                indirect_slots = SLOTS_PER_TABLE
                while indirect_slots > 0:
                    indirect_slots -= 1

                    # Create a direct pointer table and fill its entries with direct pointers to file blocks
                    tables.append("direct"); remaining_file_blocks -= SLOTS_PER_TABLE

                    # Always check if most recently added direct pointer table was enough to satisfy all file blocks
                    if remaining_file_blocks <= 0:
                        return len(tables)

    return len(tables)


def find_total_bytes():
    """This will have to be something different if not all tables are 15"""
    return find_index_blocks(FILE_BLOCKS) * ENTRY_SIZE_BYTES * SLOTS_PER_TABLE


def num_searches():
    """Basically you count "nodes" + "edges" in shortest path to the file block pointer"""

    # If small file (all block pointers in inode)
    if 0 <= FILE_BLOCKS <= DIRECT_IN_INODE:
        return 1

    # Single indirect:
    if DIRECT_IN_INODE < FILE_BLOCKS <= (DIRECT_IN_INODE + SLOTS_PER_TABLE):
        return 3

    # Double indirect:
    if (DIRECT_IN_INODE + SLOTS_PER_TABLE) < FILE_BLOCKS <= ((DIRECT_IN_INODE + SLOTS_PER_TABLE) + SLOTS_PER_TABLE ** 2):
        return 5

    # Triple indirect:
    if ((DIRECT_IN_INODE + SLOTS_PER_TABLE) + SLOTS_PER_TABLE ** 2) < FILE_BLOCKS <= float("inf"):
        return 7

    return "Should never get this string"


if __name__ == "__main__":
    print("Total bytes =", find_total_bytes(), "\nIndex blocks =", find_index_blocks(FILE_BLOCKS), "\nRequired searches =", num_searches())
