def generate_matrices(input_dir = 'data/'):
    f=open(input_dir+'A_directed.txt','w')
    newmatrix="""
0 1 1 0 0 0
1 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
0 0 0 0 1 0
""".strip()
    f.write(newmatrix)
    f.close()
    f=open(input_dir+'A_undirected.txt','w')
    newmatrix="""
0 1 1 1 0 0
1 0 1 0 0 0
1 1 0 0 0 0
1 0 0 0 1 0
0 0 0 1 0 1
0 0 0 0 1 0
""".strip()
    f.write(newmatrix)
    f.close()
    f=open(input_dir+'D_undirected_weighted.txt','w')
    newmatrix="""
0 2 5 3 0 0
2 0 7 0 2 0
5 1 0 0 2 0
3 0 0 0 2 0
0 2 2 2 0 1
0 0 0 0 1 0
""".strip()
    f.write(newmatrix)
    f.close()
    f=open(input_dir+'B_directed.txt','w')
    newmatrix="""
0 1 1 1 0 0 0 0
1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 1
0 0 0 0 1 0 1 0
0 0 0 1 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0
""".strip()
    f.write(newmatrix)
    f.close()
    f=open(input_dir+'B_undirected.txt','w')
    newmatrix="""
0 1 1 1 0 0 0 0
1 0 1 0 0 0 0 0
1 1 0 0 0 0 0 1
1 0 0 0 1 0 1 0
0 0 0 1 0 1 0 0
0 0 0 0 1 0 1 0
0 0 0 1 0 1 0 1
0 0 1 0 0 0 1 0
""".strip()
    f.write(newmatrix)
    f.close()

    f=open(input_dir+'C_undirected.txt','w')
    newmatrix="""
0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1
0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0
""".strip()
    f.write(newmatrix)
    f.close()
generate_matrices()

## more at  http://graphonline.ru/en/graphs_examples