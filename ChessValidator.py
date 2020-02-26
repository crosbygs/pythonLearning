chessBoard={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '6e': 'wking', '3g':'bbishop'}

def isValidChessBoard(boardDictonary):

  validPieceCount={'bking':1,'wking':1,'bqueen':1,'wqueen':1,'bbishop':2,'wbishop':2,'bknight':2,'wknight':2,'brook':2,'wrook':2,'bpawn':8,'wpawn':8}

  for k in boardDictonary.keys():
    if int(k[0])<=8:
      if k[1] in ['a','b','c','d','e','f','g','h']:
        blnPositionValid=True
      else:
        blnPositionValid=False
        break
    else:
      blnPositionValid=False
      break
  if not blnPositionValid:
    return False
  else:
    #Now, check the pieces
    for k,v in validPieceCount.items():
      intPieceCount = sum(x==k for x in boardDictonary.values())
      print(k+str(intPieceCount))
      if intPieceCount > v:
        blnPieceCountValid=False
        break
      else:
        blnPieceCountValid=True
    if blnPieceCountValid:
      return True
    else:
      return False

if isValidChessBoard(chessBoard):
  print('The board looks great!')
else:
  print('You have something messed up with the board.')

    