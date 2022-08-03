import sys

N=int(input())
L=list(map(int, sys.stdin.readline().split()))

list(map(lambda x : x-min(L), L))
