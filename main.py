from new import taxtest;
from new import sum; 
from new import x;
import numpy as np

a=np.arange(10);

print(a);


print(sum(1, 2));
print("hello world");

print(taxtest());


def random(x):
    x.append(6);
    return x;

print(random(x));