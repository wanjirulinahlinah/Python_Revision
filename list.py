# Write a Python program to find the length of a list.

def find_length(my_list):
    length = 0
    for _ in my_list:
        length += 1
    return length

my_list = [1, 2, 3, 4, 5]
print(find_length(my_list))  # Output: 5

# Write a Python program to find the sum of all elements in a list.

def find_sum(my_list):
    total=0
    for num in  my_list:
        total+=num
    return total
my_list = [1, 2, 3, 4, 5]
print(find_sum(my_list))   

# Write a Python program to find the largest element in a list.
def largest_element(my_list):
    largest = my_list[0]
    for num in my_list:
        if num > largest:
            largest=num
    return largest
my_list =[1,2,3,4,5]  
print(largest_element(my_list))  

# Write a Python program to remove duplicates from a list.

def remove_duplicates(my_list):
    unique_list=[]
    for element in my_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
my_list=[1,2,3,2,4,1,5] 
print(remove_duplicates(my_list))       
    
    # The Ever-changing Ankara: You are a fashion designer known for your unique and vibrant Ankara Designs.
    # Recently you've discovered that some of your fabric patterns change their design based on the temperature 
    # and mood of the wearer. You want to create a software application that can predict changes in the fabric design
    # given the mood and temperature data. Think about the classes you will need to model the changing Ankara and how 
    # to predict the changes. I want to do this question using a Python program. 
 
class AnkaraFabric:
    def __init__(self, design, temperature_thresholds, mood_thresholds):
        self.design = design
        self.temperature_thresholds = temperature_thresholds
        self.mood_thresholds = mood_thresholds

    def get_design(self, temperature, mood):
        temperature_class = self.get_temperature_class(temperature)
        mood_class = self.get_mood_class(mood)
        return self.design[temperature_class][mood_class]

    def get_temperature_class(self, temperature):
        for threshold in self.temperature_thresholds:
            if temperature < threshold:
                return threshold
        return self.temperature_thresholds[-1]

    def get_mood_class(self, mood):
        for threshold in self.mood_thresholds:
            if mood < threshold:
                return threshold
        return self.mood_thresholds[-1]


class AnkaraDesignPredictor:
    def __init__(self, fabric):
        self.fabric = fabric

    def predict_design(self, temperature, mood):
        return self.fabric.get_design(temperature, mood)
    
    
class AnkaraFabric:
        def __init__(self, design, temperature_thresholds, mood_thresholds):
            self.design = design
            self.temperature_thresholds = temperature_thresholds
            self.mood_thresholds = mood_thresholds

        def get_design(self, temperature, mood):
            temperature_class = self.get_temperature_class(temperature)
            mood_class = self.get_mood_class(mood)
            return self.design[temperature_class][mood_class]
        def get_temperature_class(self, temperature):
            for threshold in self.temperature_thresholds:
                if temperature < threshold:
                    return threshold
                return self.temperature_thresholds[-1]
            
            def get_mood_class(self, mood):
                for threshold in self.mood_thresholds:
                    if mood < threshold:
                        return threshold
                    return self.mood_thresholds[-1]


class AnkaraDesignPredictor:
    def __init__(self, fabric):
        self.fabric = fabric

    def predict_design(self, temperature, mood):
        return self.fabric.get_design(temperature, mood)
    
    fabric_design = {
    20: {
        1: "Design A",
        2: "Design B"
    },
    30: {
        1: "Design C",
        2: "Design D"
    }
}

temperature_thresholds = [25]
mood_thresholds = [1.5]

# Create an instance of AnkaraFabric
fabric = AnkaraFabric(fabric_design, temperature_thresholds, mood_thresholds)

# Create an instance of AnkaraDesignPredictor
predictor = AnkaraDesignPredictor(fabric)

# Predict the fabric design based on temperature and mood
temperature = 28
mood = 1.2

predicted_design = predictor.predict_design(temperature, mood)
print(predicted_design)  # Output: Design C
