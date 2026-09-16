class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #diff prereq ->courses it unlocks
        #res course -> no.prereq
        diff = {}
        res = [0] * numCourses

        #counts number of prereqs for each course, and maps each prereq to course 
        #it unlocks
        def initial(pres):
            for a,b in pres:
                res[a] += 1
                diff[b] = diff.get(b, []) + [a]
        initial(prerequisites)

        #finds courses with no prerequisites
        queue = deque([])
        for i in range(numCourses):
            if res[i] == 0:
                queue.append(i)

        while(len(queue) != 0):
            #course already unlocked
            node = queue.popleft()

            for course in diff.get(node, []):
                res[course] -= 1
                if res[course] == 0:
                    queue.append(course)

        
        for val in res:
            if val != 0:
                return False
        return True

