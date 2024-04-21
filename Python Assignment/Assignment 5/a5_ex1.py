def sub_summarize(nested: list, sub_sums: list) -> int:
    
    sumAll = 0

    for item in nested:
        if isinstance(item, list):
            # Recursively calculate the sum of nested sublists

            sub_sum = sub_summarize(item, sub_sums)
            sumAll += sub_sum
        else:
            sumAll += item

    sub_sums.append(sumAll)
    return sumAll



nested = [1, 2, 3, [4, [5, 6], 7], 8, [9, 10]]
sub_sums = []
total_sum = sub_summarize(nested, sub_sums) 
print(total_sum)
print(sub_sums)  