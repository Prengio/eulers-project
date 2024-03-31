#rather than cycle through all number below 1000 it's easier to just sum the multiples of 3 and 5 and subtract the multiples of 15 using euler's summation formula
target = 999
def sumdiv(x):
  p=target//x
  return (p*(p+1)*x)/2
print(sumdiv(3)+sumdiv(5)-sumdiv(15))