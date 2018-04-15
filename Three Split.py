def halfsplit(array,amt):
    count = 0
    cur_sum = 0
    for pos,num in enumerate(array[:len(array)-1]):
        cur_sum += num
        if cur_sum == amt:
            print(cur_sum)
            count += 1
    return count

def threeSplit(a):
    summation = sum(a)
    piece = summation/3
    curr_sum = 0
    answer = 0
    for position,number in enumerate(a):
        curr_sum += number
        if curr_sum == piece:
            answer += halfsplit(a[position+1:],piece)
    return answer
