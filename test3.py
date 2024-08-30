def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate the area between the two lines
        width = right - left
        water = min(height[left], height[right]) * width
        max_water = max(max_water, water)
        
        # Move the pointer with the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

# Example usage
height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))  # Output: 49



from collections import defaultdict
def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    # Group words by their sorted version as the key
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    # Return the grouped anagrams
    return list(anagrams.values())

# Example usage
strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]



def merge(intervals):
    # Sort the intervals by the starting time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for interval in intervals:
        # If merged is empty or there is no overlap, add the current interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is overlap, so merge the current interval with the previous one
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))  # Output: [[1,6],[8,10],[15,18]]
