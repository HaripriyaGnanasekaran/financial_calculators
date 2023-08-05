
# self.data[monte_carlo_df].iloc[-1].plot(kind="hist", bins=500)
self.data[monte_carlo_df]["PredictedMeanStockPrice"] = self.data[monte_carlo_df].mean(axis=1)
self.data[monte_carlo_df]["PredictedMeanStockPrice"].plot()
plt.show()
print(self.data[monte_carlo_df]["PredictedMeanStockPrice"].iloc[-1], "<mean>")

terminal_width, _ = shutil.get_terminal_size()
line = "= " *terminal_width
sp = self.data[metrics_dict][cv.current_stock_price]

var = self.data[monte_carlo_df].iloc[-1].quantile(0.05)
print(f"$ {( 1 -va r /sp ) *p.current_value:.2f} of your Value is at Risk in {p.years_to_simulate} years")
print(f"95% chance the price will be > $ {p.current_valu e *va r /sp:.2f}$")
print(f"95% chance expected return > {((va r /sp) - 1 ) *100:.2f} %")
print(line)