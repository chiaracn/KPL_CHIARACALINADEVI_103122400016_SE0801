from memory_profiler import profile

@profile
def proses_memori():
    data = [x * 2 for x in range(1000000)]
    return sum(data)

    if _name_ == "_main_":
        proses_memori()