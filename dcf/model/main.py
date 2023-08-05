import time
from calculation import Calculation
from calculation.dataset.dataset import Dataset as d
from calculation.variables.levels import metrics_dict

start = time.time()
Calculation.execute()
end = time.time()

print(f"Finished: Took {(end-start):.2f} seconds.")
print(d.data[metrics_dict])