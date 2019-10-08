class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dic = {}
        island = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print('i: ',i, '     j: ',j, '    dic: ',dic)
                if board[i][j] == 'O':
                    isl1 = 0
                    isl2 = 0
                    if i-1>-1 and board[i-1][j] == 'O':
                        isl1 = dic[(i-1,j)]
                    if j-1 > -1 and board[i][j-1] == 'O':
                        # print(str(i)+str(j-1))
                        isl2 = dic[(i,j-1)]
                    if isl1 == isl2 and isl1 == 0:
                        island += 1
                        dic[(i,j)] = island
                    elif isl1 == 0 or isl2 == 0:
                        dic[(i,j)] = max(isl1,isl2)
                    elif isl1 == isl2:
                        dic[(i,j)] = isl1
                    else:
                        dic[(i,j)] = min(isl1,isl2)
                        for key in dic:
                            if dic[key] == max(isl1,isl2):
                                dic[key] = min(isl1,isl2)
        print('dic: ', dic)
        dic1 = {}
        for k in dic:
            if dic[k] not in dic1:
                dic1[dic[k]] = []
                dic1[dic[k]].append(k)
            else:
                dic1[dic[k]].append(k)
        print('dic1: ', dic1)
        noisld = {}
        for k in dic1:
            for loc in dic1[k]:
                if int(loc[0]) == 0 or int(loc[0]) == len(board)-1 or int(loc[1] )== 0 or int(loc[1]) == len(board[0])-1:
                    if k not in noisld:
                        noisld[k] =1
        print('noisld: ',noisld)
        for k in dic1:
            if k not in noisld:
                for loc in dic1[k]:
                    board[int(loc[0])][int(loc[1])] = 'X'
        return board
