price = float(input())
perc_disc = float(input())
disc = price * (perc_disc/100)
total = price - disc
print (f"O desconto é de R$ {disc:.2f}, o valor final do produto é R$ {total:.2f}")
