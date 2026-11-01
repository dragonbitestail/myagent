from functions.write_file import write_file

# write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#write_file("calculator", "/tmp/temp.txt", "this should not be allowed")


tests = [
    ["lorem.txt", "wait, this isn't lorem ipsum"],
    ["pkg/morelorem", "lorem ipsum dolor sit amet"],
    ["/tmp/temp.txt", "this should not be allowed"],
]
for tt in tests:
    print(write_file("calculator", tt[0], tt[1]))
