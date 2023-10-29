# @param {List[List[int]]} matrix
# @return {List[int]}
def walk_matrix(matrix):
  # Your solution here
        result = []

        start_row = 0
        end_row = len(matrix) - 1
        start_column = 0
        end_column = len(matrix[0]) - 1

        while(end_row >= start_row and end_column >= start_column):
                
                for column in range(start_column, end_column+1):
                        result.append(matrix[start_row][column])
                
                start_row+=1

                if(end_row >= start_row and end_column >= start_column):
                    for row in range(start_row, end_row+1):
                            result.append(matrix[row][end_column])
                    end_column-=1

                if(end_row >= start_row and end_column >= start_column):
                    for column in range(end_column, start_column-1, -1):
                            result.append(matrix[end_row][column])
                    end_row-=1
                

                if(end_row >= start_row and end_column >= start_column):
                    for row in range(end_row, start_row-1, -1):
                            result.append(matrix[row][start_column])
                    start_column+=1
        
        return result 
                


                




    
