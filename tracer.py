#Programme to trace
#Lebogang Salagae
#5 May 2024

# check if there are trace statements in the content
def tracer_1(content):
    debug_marker = '"""DEBUG"""'
    has_traces = False
    lines = content.split("\n")
    for line in lines:
        if debug_marker in line:
            has_traces = True
            break
    return has_traces

# insert trace statements at the beginning of each function and at the top of the file
def insert_trace(content):
    traced_lines = []
    lines = content.split("\n")
    debug_added = False
    
    for line in lines:
        if not debug_added:
            traced_lines.append('"""DEBUG"""')  
            debug_added = True
        
        stripped_line = line.strip()
        
        if stripped_line.startswith("def "):
            func_name = stripped_line.split("(")[0].replace("def ", "").strip()
            traced_lines.append(line)
            traced_lines.append(f'"""DEBUG"""; print("{func_name}")')
        else:
            traced_lines.append(line)
    
    return "\n".join(traced_lines)

# remove trace statements from the content
def remove(content):
    untraced_lines = []
    lines = content.split("\n")
    in_trace_mode = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if stripped_line == '"""DEBUG"""':
            in_trace_mode = not in_trace_mode  
            continue
        
        if in_trace_mode and stripped_line.startswith('"""DEBUG""";'):
            continue
        
        untraced_lines.append(line)
    
    return "\n".join(untraced_lines)

def main():
    print("***** Program Trace Utility *****")
    file_name = input("Enter the name of the program file: ").strip()
    
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        
        if tracer_1(content):
            print("Program contains trace statements")
            print("Removing...", end=" ")
            new_content = remove(content)  # remove traces
        else:
            print("Inserting...", end=" ")
            new_content = insert_trace(content)  # insert traces
        
        with open(file_name, 'w') as file:
            file.write(new_content)
        
        print("Done")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

if __name__ == "__main__":
    main()