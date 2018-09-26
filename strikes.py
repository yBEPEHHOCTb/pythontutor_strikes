days,number_of_parties=list(map(int,input().split()))
strike_sets=set()
for party in range(number_of_parties):
    strike_day,strike_freqs=list(map(int,input().split()))
    while strike_day<=days:
        if strike_day!=6 and strike_day!=7:
            strike_sets.add(strike_day)
        strike_day+=strike_freqs
