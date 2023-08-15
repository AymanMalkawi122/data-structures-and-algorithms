# business trip

## Task: Write a function called business trip to Determine whether the trip is possible with direct flights, and how much it would cost

## 1. Whiteboard Process

![image](./assets/Screenshot%202023-08-15%20044317.png)

## 2. Approach & Efficiency

### Approach

1. Iterate through the array of city names.
2. For each pair of consecutive cities, check if there is a direct flight between them.
3. If a direct flight exists, add the cost of the flight to the total cost.
4. If a direct flight doesn't exist for any pair of cities, return None to indicate that the trip is not possible.
5. After iterating through all city pairs, return the total cost if the trip is possible, or None if it's not.

### Efficiency

***Space Complexity:***

 The space complexity of the business_trip function is O(n), as it stores the neighbors of the current city in a variable.

***Time Complexity:***

The time complexity of the business_trip function is O(n), where n is the number of cities in the array. In the worst case, we need to check for a direct flight for each consecutive pair of cities.

## 3. Solution

* The business_trip function determines whether a trip is possible with direct flights between consecutive cities and calculates the total cost of the trip if it's possible. It achieves this by iterating through the array of city names and checking for direct flights between each pair of consecutive cities. If a direct flight is found, the cost of the flight is added to the total cost. If no direct flight is found for any pair of cities, the function returns None to indicate that the trip is not possible.
