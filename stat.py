def calc_chi(train):
	target = train.churn
	need_calc = train.select_dtypes(object, int).columns
	new_list = []
	p_val = []

	for c in enumerate(need_calc):
		observed = pd.crosstab(c, target)
		chi2, p, degf, expected = sp.stats.chi2_contingency(observed)
		if p < 0.05:
			new_list.append(c)
			p_val.append(p)
	return new_list, p_val


from scipy.stats import chisquare

train['p'] = chisquare(train.select_dtypes(object, int), axis=1)[1]

train['same_diff'] = np.where(train['p'] > 0.05, 'same', 'different')