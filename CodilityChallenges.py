class Solutions():

    # HexSpeak
    def HexSpeakSolution(self, s):
        N = int(s)
        H = hex(N).strip("0x")
        H.upper()
        H = H.replace('0', 'O')
        H = H.replace('1', 'I')

        hex_letters = ["A","B","C","D","E","F","I","O"]
        for i in H:
            if i not in hex_letters:
                return "ERROR"
        return H

    # hs = Solutions()
    # print(hs.HexSpeakSolution("257"))


    # Students
    def Students(self, A):

        for i in range(1, len(A) - 1):
            current_student = A[i]
            prev_student = A[i - 1]
            next_student = A[i + 1]

            if prev_student > current_student and next_student > current_student:
                A[i] += 1
            elif current_student > prev_student and current_student > next_student:
                A[i] -= 1

        return  A

# s = Solutions()
# print(s.Students([1, 6, 3, 4, 3, 5]))


    # Unique substrings
    def UniqueSubstrings(self, s):
        # Count construct
        # not correct
        string = s.lower()
        count = 1
        identicalChar = 0

        for i in range(len(string) - 1):
            count += 1

            if string[i] == string[i-1]:
                identicalChar += 1
            else: identicalChar = 0

            if identicalChar > 0:
                count += identicalChar

        return count

# us = Solutions()
# print(us.UniqueSubstrings("zzzyz"))


    # earliest index that frog can jump the river
    def FrogRiverOne(self, X, A):
        set_temp = set([i for i in range(1, X + 1)])

        for i in A:
            if i in set_temp:
                set_temp.remove(i)
                if len(set_temp) == 0:
                    return A.index(i)
        return -1


# fro = Solutions()
# print(fro.FrogRiverOne( 5, [1,3,1,4,2,3,5,4] )) # 6
# print(fro.FrogRiverOne( 2, [1,3,1,4,2,3,5,4] )) # 4
# print(fro.FrogRiverOne( 1, [1] )) # 0


    # smallest missing positive int
    def MissingInteger(self, A):
        if len(A) == 0:
            return 1

        smallest_int = 1
        set_a = set(A)

        while smallest_int in set_a:
            smallest_int += 1

        return smallest_int

# mi = Solutions()
# print(mi.MissingInteger( [1,3,6,4,1,2] )) # 5
# print(mi.MissingInteger( [1,2,3] )) # 4
# print(mi.MissingInteger( [-1,-3,0] )) # 1


    # calcualte value of counters after applying operations
    def MaxCounters(self, N, A):
        counters = [0] * N
        max_result = max_counter = 0

        for i in range(len(A)):
            if A[i] == N + 1:
                max_result = max(max_result, max_counter)
            else:
                if counters[A[i] - 1] < max_result:
                    counters[A[i] - 1] = max_result

                counters[A[i] - 1] += 1
                max_counter = max(max_counter, counters[A[i] - 1])

        for i in range(N):
            counters[i] = max(max_result, counters[i])

        return counters


# mx = Solutions()
# print(mx.MaxCounters( 5, [3,4,4,6,1,4,4] )) # [ 3,2,2,4,2 ]


    def PassingCars(self, A):
        count = 0
        passes = 0

        for i in A:
            if i == 0:
                count += 1
            else:
                passes += count
            # handle max passing cars
            if len(A) > 100000 or passes > 1000000000:
                return - 1

        return passes


# pc = Solutions()
# print(pc.PassingCars( [0, 1, 0, 1, 1] )) # 5


    # final the minimum nucleotide in a range sequence of DNA
    def GenomicRangeQuery(self, S, P, Q):
        impact_factor = []

        # solution 1
        letters = [ "A", "C", "G", "T" ]
        dict_temp = { val:i+1 for i, val in enumerate(letters) }

        for i in range(len(P)):
            for key in dict_temp:
                if key in (S[P[i]:Q[i] + 1]):
                    impact_factor.append(dict_temp[key])
                    break

        # solution 2
        for i in range(len(P)):
            # substrings P : Q
            if "A" in (S[P[i]:Q[i] + 1]):
                impact_factor.append(1)
            elif "C" in (S[P[i]:Q[i] + 1]):
                impact_factor.append(2)
            elif "G" in (S[P[i]:Q[i] + 1]):
                impact_factor.append(3)
            else:
                impact_factor.append(4)

        return impact_factor


grq = Solutions()
print(grq.GenomicRangeQuery( "CAGCCTA", [2,5,0], [4,5,6] )) # 2 4 1
