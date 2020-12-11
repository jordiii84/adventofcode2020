class Color:
    def __init__(self, name, parents=None, childs=None):
        self.name = name
        self.parents = []
        if parents:
            for parent in parents:
                self.add_parent(parent=parent)
        self.childs = []
        if childs:
            for child in childs:
                self.add_child(child=child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.childs.append(child)

def parse_childs(line):
    if "no" in line:
        return None
    else:
        colors_splitted = line.split(",")
        colors=[]
        for color in colors_splitted:
            colors.append(color.strip().split(" ")[1] + " " +color.strip().split(" ")[2])
        return colors
    # elif

def create_colors(lines):
    colors={}
    for line in lines:
        line=line.strip("\n")
        main_color = line.split(" bags contain")[0]
        if main_color not in colors.keys():
            color = Color(name=main_color)
            colors[main_color]=color
    return colors

def fill_parents_childs(line, colors):
    main_color = line.split(" bags contain")[0]
    child_colors = parse_childs(line=line.split(" bags contain")[1])
    if child_colors:
        for child_color in child_colors:
            if child_color in colors.keys():
                colors[child_color].add_parent(parent=main_color)
            colors[main_color].add_child(child=child_color)
    return colors

def get_parents(childs, colors):
    parents = []
    for child in childs:
        parents += colors[child].parents
    return parents


file1 = open('input.txt', 'r')
Lines = file1.readlines()

colors = create_colors(lines=Lines)
for line in Lines:
    line = line.strip("\n")
    colors_temp = fill_parents_childs(line=line, colors=colors)
    colors = colors_temp

for color in colors.values():
    print(f"Color {color.name}")
    print(f" - Childs {color.childs}")
    print(f" - Parents {color.parents}")

parents = get_parents(childs = ["shiny gold"], colors=colors)
total_parents = parents
while len(parents) != 0:
    parents = get_parents(childs=parents, colors=colors)
    total_parents += parents
print(f"--------Number of parents {len(total_parents)}")
print(f"--------Number of parents (set) {len(set(total_parents))}")