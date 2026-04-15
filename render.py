"""
Code written by Lynn van der Luit
april 2026

renders the original joints and members using matplotlib
"""

def main():
    import json
    import matplotlib.pyplot as plt

    with open("joints0.json", "r") as file:
        joints0 = json.load(file)
    
    with open("members.json", "r") as file:
        members = json.load(file)



    fig, ax = plt.subplots(1, 1)
    #ax.grid()
    ax.set_aspect('equal', adjustable='box')


    ax.scatter(*list(zip(*joints0)), color="k")

    for member in members:
        p0 = joints0[member[0]]
        p1 = joints0[member[1]]
        plt.plot(*list(zip(p0, p1)), color="k")
    plt.show()



if __name__ == "__main__":
    main()