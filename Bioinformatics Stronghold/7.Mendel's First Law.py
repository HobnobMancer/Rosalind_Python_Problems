# http://rosalind.info/problems/iprb/
# GIVEN: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# RETURN: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Define population groups
k = 2 # number of homozygous dominant individuals
m = 2 # number of heterozygous individuals
n = 2 # number of homozygous recessive individuals

# Calculating probability of individual having dominant phenotype
# when first mate is k and second mate is k
FkSk = (k / (k+m+n)) * ((k-1) / ((k-1)+m+n))

# when first mate is k and second mate is m
FkSm = (k / (k+m+n)) * (m / ((k-1)+m+n))

# when first mate is k and second mate is m
FkSn = (k / (k+m+n)) * (n / ((k-1)+m+n))

# when first mate is m and second mate is m
FmSm = (m / (k+m+n)) * ((m-1) / (k+(m-1)+n))

# when first mate is m and second mate is k
FmSk = (m / (k+m+n)) * (k / (k+(m-1)+n))

# when first mate is m and second mate is n
FmSn = (m / (k+m+n)) * (n / (k+(m-1)+n))

# when first mate is n and second mate is n
FnSn = (n / (k+m+n)) * ((n-1) / (k+m+(n-1)))

# when first mate is n and second mate is k
FnSk = (n / (k+m+n)) * (k / (k+m+(n-1)))

# when first mate is n and second mate is m
FnSm = (n / (k+m+n)) * (m / (k+m+(n-1)))

# Probability of at least one partner being dominant, all offspring will show dominant phenotype
# Mating pairs: kk, km, mk, kn and nk
probabilityDominantMate = FkSk + FkSm + FmSk + FkSn + FnSk

# Heterozygous mating have 75% chance offspring will have dominant phenotype
probabilityHeterozygotMate = (FmSm)*0.75

# Heterozygouse with recessive have 50% offspring will have dominant phenotype
# Mating pairs: mn and nm
probabilityHeteroAndRecessive = (((FmSn)*0.5)+((FnSm)*0.5))

# total probability offspring will have dominant phenotype
# Recessive with recessive has 0 probability offspring will have dominant phenotype
dominantPhenotype = probabilityDominantMate + probabilityHeterozygotMate + probabilityHeteroAndRecessive
print(dominantPhenotype)
