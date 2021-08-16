def encode_var_labels(i,j,k, N=9):

  counter =0
  for a in range(i):
    for b in range(j):
      for c in range(k):
        pass
  return (a*N*N) + (b*N) + c + 1

  def decode_var_labels(index, N=9):
    for i in range(N):
      for j in range(N):
        for k in range(N):
          if (i*N*N) + (j*N) + k + 1 == index:
            return [i+1 , j+1 , k+1 ]
