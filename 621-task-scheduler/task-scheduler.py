from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequencies
        freq = Counter(tasks)
        
        # Step 2: Max-heap using negative frequencies
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)
        
        # Step 3: Cooldown queue: (available_time, task_count)
        cooldown = deque()
        time = 0
        
        while max_heap or cooldown:
            time += 1

            # Step 4: Re-add from cooldown if cooldown expired
            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(max_heap, count)
            
            # Step 5: Run task if available
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # decrement since we're using negative values
                if count != 0:
                    # Add to cooldown with available_time = time + n + 1
                    cooldown.append((time + n + 1, count))

        return time
