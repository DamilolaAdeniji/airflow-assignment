
def create_output_file(filename):
    with open(filename, 'w'):
        pass 


def read_lines(filepath,start_line,end_line,output_file):
    """
    filepath:(str) path to the .txt file you intend to loop over
    start_line: (int) the position of the line you intend to start looping from
    end_line: (int) the position of the line you intend to end with
    """

    with open(output_file, 'a') as target: # open the target file

        with open(filepath, 'r') as f: # open the source file
            name_list = [' amazon ',' apple ',' facebook ',' google ',' microsoft ']
            for i, line in enumerate(f):
                if start_line <= i < end_line:
                    if any(word in line.lower() for word in name_list):
                        target.write(line)
                    else:
                        continue
                elif i >= end_line:
                    break


def file_read_engine(num,filepath,output_file):
    start = 1
    end = start + num
    with open(filepath, 'r') as file:
        total_lines = sum(1 for _ in file)
    print (total_lines)
    while True:
        print (f'Starting point: {start}, End_point: {end}')
        status = read_lines(filepath,start,end,output_file)
        start = end
        end = end + num
        if start>total_lines:
            break
    print ('done with the scan')
#    print (f'Succesfully scanned {read_so_far} lines of data')