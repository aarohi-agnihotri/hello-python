# WHY yield? — the problem return causes
#
# STEP 1 — using return inside loop:
# def even_generator(limit):
#     for i in range(2, limit+1, 2):
#         return i                 # exits after FIRST value (2), loop never continues
#
# STEP 2 — list workaround:
# def even_generator(limit):
#     li = []
#     for i in range(2, limit+1, 2):
#         li.append(i)
#     return li                    # works but stores ALL values in memory at once
#                                  # defeats the purpose — not generating one by one
#
# a generator object is what Python returns when you call a generator function (one that uses yield)
# generator object is a lazy iterator that Python creates automatically when a function has yield. it holds the state and produces values one by one on demand.
# STEP 3 — TypeError:
# for num in even_generator(10)    # if function uses return, it gives back a list/int
#                                  # not a generator object — TypeError: not iterable
#
# SOLUTION — yield:
# yield sends one value at a time, pauses the function, saves its state
# next time loop asks for value, function resumes exactly where it left off
# Python handles all state/memory management automatically
# perfect for large/infinite sequences — no need to store everything in memory


# MEMORY BEHIND yield — think from memory perspective
#
# return approach:
# stores ALL values in memory at once before giving anything back
# if limit = 10000000, creates a list of 10000000 items in RAM immediately
# then dumps everything and terminates — function state is gone
#
# yield approach:
# only ONE value lives in memory at a time
# function state is preserved in memory (current value of i, where loop is)
# when next value is needed — resumes from exact same point, not from start
# when done — state is cleared automatically
#
# visual difference:
# return → [2, 4, 6, 8, 10] — entire list in RAM at once
# yield  → 2 ... 4 ... 6 ... 8 ... 10 — one at a time, rest not in memory yet
#
# real world case — why it matters:
# reading a file with 1 million lines
# return → loads all 1 million lines into RAM at once — can crash
# yield  → reads one line at a time — memory stays low, program stays fast

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)
# output: 2 4 6 8 10