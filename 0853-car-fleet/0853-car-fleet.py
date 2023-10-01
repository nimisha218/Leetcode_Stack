class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        # Let's make a dictionary with key: positions, values: speed

        car_fleet = {}
        for i in range(len(position)):
            car_fleet[position[i]] = speed[i]
        
        # print("Car Fleet dictionary: ", car_fleet)

        # Now, let's sort the dictionary based on the keys (positions)
        car_positions = list(car_fleet.keys())
        car_positions.sort(reverse=True)

        car_fleet = {i: car_fleet[i] for i in car_positions}

        # print("Sorted car fleet: ", car_fleet)
        # print()

        # Now, let's convert the dictionary to a list of pairs
        cars = []
        for position in car_fleet:
            cars.append([position, car_fleet[position]])
        
        # print("Cars list: ", cars)
        # print()
            
        # Now, let's start calculating the number of car fleets

        for i in range(len(cars)):

            time_taken = (target - cars[i][0]) / cars[i][1]
            # print("Time taken to reach position: ", time_taken)

            if stack and time_taken <= stack[-1]:
                # Do nothing since we won't be adding this to the stack
                pass 
            
            else:
                stack.append(time_taken)
    
        return len(stack)