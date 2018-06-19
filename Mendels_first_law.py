# Given : Three positive integers k,m,n representing a population consisting of k+m+n organisms; k = AA, m = Aa, n = aa (A being the dominant allele)
# Return : The probability that two randomly selected mating organisms will produce an individual possessing the dominant phenotype

print "Enter the number of dominant homozygotes, heterozygotes, recessive homozygotes (Hit the Return key after every entry)"
k, m, n = float(raw_input()), float(raw_input()), float(raw_input())
sum = float(k + m + n)          #total size of the population

# Calculating the probability that the offspring will be recessive
# Only nxn, mxn & nxm matings will give rise to recessive progeny, hence by addition of the probabilities obtained in the three cases we get,

p_recessive = ((n**2) - (n) + (0.25*(m**2)) - (0.25*(m)) + (m*n))/ ((sum)*(sum - 1)) 

p_dominant = 1 - p_recessive
print "Probability of a dominant phenotype: ", p_dominant