from scipy.stats import f_oneway

# Sample data for three groups
group1 = [5, 7, 3, 4, 8]
group2 = [9, 12, 11, 13, 10]
group3 = [14, 16, 19, 17, 15]

# Perform ANOVA
f_statistic, p_value = f_oneway(group1, group2, group3)

# Print the results
print("F-statistic:", f_statistic)
print("p-value:", p_value)