num_customers = int(input())

# Initialize lists to store the times for each type of purchase
purchase_a_time = [0] * 5001
purchase_b_time = [0] * 5001
purchase_c_time = [0] * 5001

for i in range(1, num_customers+1):
    purchase_a_time[i], purchase_b_time[i], purchase_c_time[i] = map(int, input().split())

# Initialize a list to store the minimum time to serve each customer up to that point
min_time = [0] * (num_customers+1)

# Set the minimum time for the first customer to their purchase time for type A
min_time[1] = purchase_a_time[1]

# If there are more than one customer, set the minimum time for the second customer
if num_customers > 1:
    min_time[2] = min(purchase_a_time[1] + purchase_a_time[2], purchase_b_time[1])

# For each customer after the first two, set the minimum time to serve them 
for i in range(3, num_customers+1):
    min_time[i] = min(min_time[i-1] + purchase_a_time[i], 
                      min_time[i-2] + purchase_b_time[i-1], 
                      min_time[i-3] + purchase_c_time[i-2])

# Print the minimum time to serve all customers
print(min_time[-1])
