"""
Code written by Lynn van der Luit
april 2026

code generates testdata and puts them into json files
"""

def main():
    import json

    joints = [
        [0, 0],
        [1, 1],
        [2, 0],
        [2, 2],
        [4, 0],
        [4, 2],
        [5, 1],
        [6, 0],
        [6, 2],
        [8, 0],
        [8, 2],
        [9, 1],
        [10, 0]
    ]

    members = [
        [0, 1],
        [0, 2],
        [1, 2],
        [1, 3],
        [2, 3],
        [2, 4],
        [3, 4],
        [3, 5],
        [4, 5],
        [4, 6],
        [4, 7],
        [5, 6],
        [5, 8],
        [6, 7],
        [6, 8],
        [7, 8],
        [7, 9],
        [7, 10],
        [8, 10],
        [9, 10],
        [9, 11],
        [9, 12],
        [10, 11],
        [11, 12]
    ]

    force_displacement = [
        [None, None, 0, 0],
        [0, 0, None, None],
        [0, -1, None, None],
        [0, 0, None, None],
        [0, -1, None, None],
        [0, 0, None, None],
        [0, 0, None, None],
        [0, -1, None, None],
        [0, 0, None, None],
        [0, -1, None, None],
        [0, 0, None, None],
        [0, 0, None, None],
        [0, None, None, 0]
    ]

    with open("joints0.json", "w") as file:
        json.dump(joints, file)
    
    with open("members.json", "w") as file:
        json.dump(members, file)

    with open("force_displacement.json", "w") as file:
        json.dump(force_displacement, file)

if __name__ == "__main__":
    main()