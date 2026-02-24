import matplotlib.pyplot as plt
import numpy as np
import datetime

#real data registered by myself since i've started dieting and exercising.
date_strings = ['15/01/2025', '30/01/2025', '08/02/2025', '17/02/2025', '21/03/2025',
                 '22/03/2025', '23/03/2025', '24/03/2025', '25/03/2025', '30/03/2025']
weight = [145, 139.5, 137.9, 136.2, 131.4, 130.9, 130.2, 130.6, 132.5, 129.2]

#convert date strings to datetime objects
dates = [datetime.datetime.strptime(d, "%d/%m/%Y") for d in date_strings]

#dates to ordinal numbers
dates_ordinal = [d.toordinal() for d in dates]

#linear regression
coefficients = np.polyfit(dates_ordinal, weight, 1)
p = np.poly1d(coefficients)

#points for the regression line
ordinal_range = np.linspace(min(dates_ordinal), max(dates_ordinal), 100)
weight_regression = p(ordinal_range)

#ordinal numbers back to dates for plotting
date_range = [datetime.date.fromordinal(int(d)) for d in ordinal_range]

#plot // plt.figure() call
fig, ax = plt.subplots(figsize=(12, 5), dpi=150)

ax.plot(dates, weight, marker='o', linestyle='-', label='Weight (Kg)')
ax.plot(date_range, weight_regression, linestyle='--', color='red', label='Linear Regression Line')
ax.set_xlabel('Date')
ax.set_ylabel('Weight (Kg)')
ax.set_title('Weight Progress Over Time')
ax.legend()
ax.grid()

plt.xticks(rotation=45)
plt.xlim(dates[0], dates[-1])
plt.ylim(min(weight) - 2, max(weight) + 2)
plt.tight_layout()  #countering cutoff

plt.savefig('weight_progress_high_resolution.png', dpi=600)
plt.show()