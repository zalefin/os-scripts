import numpy as np

from inode_alloc import ENTRY_SIZE_BYTES, SLOTS_PER_TABLE


def find_index_blocks_math(n_block):
    if n_block <= 12:
        return 1
    tot_blocks = 1 # inode itself
    tot_mapped = 12
    remain = n_block - 12
    for depth in range(1,4):
        depth_max = SLOTS_PER_TABLE**depth
        if remain > depth_max:
            remain -= depth_max
            tot_mapped += depth_max
            tot_blocks += sum(SLOTS_PER_TABLE**n for n in range(depth))
        else:
            d = remain
            tot_mapped += d
            c = remain
            while c != 1:
                c = np.ceil(c/SLOTS_PER_TABLE)
                tot_blocks += c
            return int(tot_blocks)
    return int(tot_blocks)


def find_total_bytes_math(n_block):
    """This will have to be something different if not all tables are 15"""
    return find_index_blocks_math(n_block) * ENTRY_SIZE_BYTES * SLOTS_PER_TABLE


if __name__ == '__main__':
    print('Number of index blocks:', find_index_blocks_math(2000))

