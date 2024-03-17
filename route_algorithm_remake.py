import search_algorithm as greedy
import city as city

class Main:
    def __init__(self):
        print("yo")
        self.greedy = greedy.Greedy(19)
        self.greedy.search(city.city(0, 'Arad'))

    
app = Main()