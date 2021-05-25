from itertools import *


def cuboid_dimensions(x_,y_,z_,n_):
    print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n])


if __name__ == "__main__":
    x,y,z,n = (int(input()) for _ in range(4))
    cuboid_dimensions(x,y,z,n)