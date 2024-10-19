
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
            name_list = [' amazon ',' apple ',' facebook ',' google ',' micorsoft ']
            for i, line in enumerate(f):
                if start_line <= i < end_line:
                    if any(word in line.lower() for word in name_list):
                        target.write(line)
                    else:
                        continue
                    return True
                elif i >= end_line:
                    return False
                


def file_read_engine(num,filepath,output_file):
    start = 1
    end = start + num
    while True:
        status = read_lines(filepath,start,end,output_file)
        read_so_far = end
        start += num + 1
        end =+start
        if status == False:
            break
#    print (f'Succesfully scanned {read_so_far} lines of data')