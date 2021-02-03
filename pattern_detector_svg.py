#!/usr/bin/python3

def parse_svg(lines, y, i):
    svg = ""
    for y1 in range(y, len(lines) - 1, 1):
        x = lines[y]
        serial_buffer = []
        for j in range(i, len(x) - 1, 1):
            serial_buffer = (x[j:j + 5])
            if serial_buffer == "/svg>":
                svg += "/svg>"
                return svg
            elif x[j] != "\n":
                svg += x[j]       
        i = 0   
    return "Error Parsing SVG"

def detect_svgs(path):
    file = open(path, 'r')
    lines = file.readlines()
    svgs = []
    for y in range(0, len(lines) - 1, 1):
        x = lines[y]
        serial_buffer = []
        for i in range(0, len(x) - 1, 1):
            serial_buffer = (x[i:i + 4])
            if serial_buffer == "<svg":
                svgs.append(parse_svg(lines, y, i))
                print("SVG number " + str(len(svgs)) + " parsed")
                
    return svgs

def save_and_output_svgs(svgs):
    f = open("svgdump.txt", "w")
    for s in svgs:
        f.write(s)
        f.write("\n")
        print(s)
    f.close()


print("Enter file path to detect patterns of (like this \"FILE_PATH\"): ")
path = str(input())
svgs = detect_svgs(path)
save_and_output_svgs(svgs)
print("Number of svgs: " + str(len(svgs)))

