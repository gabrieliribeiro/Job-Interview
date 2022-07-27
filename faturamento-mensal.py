def percentage (state, total):
    return round(((100*state)/total),2)

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
others = 19849.53

total = sp + rj + mg + es + others

print("Porcentagem de SP:" + str(percentage(sp, total)) + '%')
print("Porcentagem de RJ:" + str(percentage(rj, total)) + '%')
print("Porcentagem de MG:" + str(percentage(mg, total)) + '%')
print("Porcentagem de ES:" + str(percentage(es, total)) + '%')
print("Porcentagem de outros faturamentos:" + str(percentage(others, total)) + '%')