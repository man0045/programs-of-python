def breakingRecords(scores):
    min_score = max_score = scores[0]
    min_count = max_count = 0
    
    for i in scores[1:]:
        if i < min_score:
            min_count+=1
            min_score = i
        if i > max_score:
            max_count+=1
            max_score = i
    
    return [max_count,min_count]