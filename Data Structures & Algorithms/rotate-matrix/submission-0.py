class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix)):
                if(i!=j):
                    temp=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp
        for i in range(0,len(matrix)):
            l=len(matrix)-1
            s=0
            while(l>s):
                temp=matrix[i][s]
                matrix[i][s]=matrix[i][l]
                matrix[i][l]=temp
                s+=1
                l-=1
           
                            
                    

                
              
        