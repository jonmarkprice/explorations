diagDiff rows = abs (sum majorDiag - sum minorDiag)
  where
    indicies  = [0..(length rows) - 1]
    majorDiag = zipWith (!!) rows indicies
    minorDiag = zipWith (!!) rows (reverse indicies)

  

