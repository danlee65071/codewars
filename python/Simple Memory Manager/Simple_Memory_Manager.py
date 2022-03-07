class MemoryManager:
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory
        self.len_mem = len(memory)
        self.memory_ind = [0 for i in range(self.len_mem)]
        self.counter = 1

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        if size > self.len_mem:
            raise Exception("Cannot allocate more memory than exists")
        available_mem = 0
        available_ptr = 0
        for i in range(self.len_mem):
            if available_mem == size:
                break
            if self.memory_ind[i] == 0:
                if available_mem == 0:
                    available_ptr = i
                available_mem += 1
            else:
                available_ptr = -1
                available_mem = 0
        if available_mem < size:
            raise Exception("Cannot allocate more memory than available")
        # while self.memory_ind[available_ptr] != 0:
        #     available_ptr += 1
        for i in range(available_ptr, size + available_ptr):
            self.memory_ind[i] = self.counter
        self.counter += 1
        return available_ptr

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        if self.len_mem - 1 < pointer < 0 or self.memory_ind[pointer] == 0:
            raise Exception('Free non allocated block')
        mark = self.memory_ind[pointer]
        # end_free_ptr = -1
        for i in range(pointer, self.len_mem):
            if self.memory_ind[i] != mark:
                # end_free_ptr = i
                break
            self.memory_ind[i] = 0
        # if end_free_ptr == -1:
        #     return
        # alloc_ptr = -1
        # for i in range(end_free_ptr, self.len_mem):
        #     if self.memory_ind[i] != 0:
        #         alloc_ptr = i
        #         break
        # if alloc_ptr == -1:
        #     return
        # for i in range(alloc_ptr, self.len_mem):
        #     self.memory_ind[pointer + i - alloc_ptr] = self.memory_ind[i]
        #     self.memory_ind[i] = 0

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        if self.len_mem <= pointer < 0 or self.memory_ind[pointer] == 0:
            raise Exception('Write error! Pointer is in unallocated memory')
        return self.memory[pointer]

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        if self.len_mem <= pointer < 0 or self.memory_ind[pointer] == 0:
            raise Exception('Write error! Pointer is in unallocated memory')
        self.memory[pointer] = value


mem = MemoryManager([None] * 64)
pointer1 = mem.allocate(32)
pointer2 = mem.allocate(32)
mem.release(pointer1)
mem.allocate(32)
