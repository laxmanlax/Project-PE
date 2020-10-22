"""
Question :
return a new sorted merged list from K sorted lists, each with size N

---
For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].
"""

# Bruteforce approcach , will be sort all lists and add to a new list and sort
# the new list

def merge(lists):
    result = []
    for slist in lists:
        result.extend(sorted(slist))
    return sorted(result)


input_list  = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
print (merge(input_list))



def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list
