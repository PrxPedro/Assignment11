import sys

def find_lowest_number(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            numbers = [line.strip() for line in f if line.strip()]
        
        if not numbers:
            with open(output_file, 'w') as f:
                f.write("No numbers found in file")
            return
        
        # Convert to floats to handle decimal numbers, but keep original string for output
        lowest = min(numbers, key=lambda x: float(x))
        
        with open(output_file, 'w') as f:
            f.write(lowest)
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 find_lowest_number.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    find_lowest_number(input_file, output_file)