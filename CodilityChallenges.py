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

mi = Solutions()
print(mi.MissingInteger( [1,3,6,4,1,2] )) # 5
print(mi.MissingInteger( [1,2,3] )) # 4
print(mi.MissingInteger( [-1,-3,0] )) # 1