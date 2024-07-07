class BankersAlgorithm:
    def __init__(self, available, max_demand, allocation):
        self.available = available
        self.max_demand = max_demand
        self.allocation = allocation
        self.n = len(max_demand)  #procesos
        self.m = len(available)   #recursos

        
        self.need = [[self.max_demand[i][j] - self.allocation[i][j] for j in range(self.m)] for i in range(self.n)]

    def is_safe(self):
        work = self.available[:]
        finish = [False] * self.n
        safe_sequence = []

        while len(safe_sequence) < self.n:
            allocated_in_this_round = False

            for i in range(self.n):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(self.m)):
                    for j in range(self.m):
                        work[j] += self.allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    allocated_in_this_round = True

            if not allocated_in_this_round:
                break

        return finish, safe_sequence

    def request_resources(self, process_number, request):
        if all(request[j] <= self.need[process_number][j] for j in range(self.m)) and all(request[j] <= self.available[j] for j in range(self.m)):

            for j in range(self.m):
                self.available[j] -= request[j]
                self.allocation[process_number][j] += request[j]
                self.need[process_number][j] -= request[j]

            finish, safe_sequence = self.is_safe()

            if all(finish):
                return True, safe_sequence
            else:
 
                for j in range(self.m):
                    self.available[j] += request[j]
                    self.allocation[process_number][j] -= request[j]
                    self.need[process_number][j] += request[j]
                return False, []

        return False, []
