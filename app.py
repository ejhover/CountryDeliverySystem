from flask import Flask, jsonify, Response
from waitress import serve

class DeliveryRoutes:
    def __init__(self):
        ''' 
        Instantiate self.routes, a dictionary of North American countries (keys) 
        and their respective adjacent countries (values)
        '''
        self.routes = {
            "CAN": ["USA"],
            "USA": ["CAN", "MEX"],
            "MEX": ["USA", "GTM", "BLZ"],
            "BLZ": ["MEX", "GTM"],
            "GTM": ["MEX", "BLZ", "SLV", "HND"],
            "SLV": ["GTM", "HND"],
            "HND": ["GTM", "SLV", "NIC"],
            "NIC": ["HND", "CRI"],
            "CRI": ["NIC", "PAN"],
            "PAN": ["CRI"]
        }

    def get_routes(self) -> dict:
        ''' 
        Return dictionary of routes
        '''
        return self.routes

    def add_country(self, new_country: str, adjacent_countries: list[str]) -> None:
        '''
        Add country and its adjacent countries to the routes dictionary
        '''
        self.routes[new_country] = adjacent_countries
        return

    def find_route(self, start: str, destination: str) -> list[str]:
        ''' 
        Find a route from the current country to the destination country
        '''
        if destination not in self.routes.keys(): # If destination is not valid
            return None

        queue = [[start]]
        visited = [start]
        if start == destination: # If already at destination, return destination
            return queue

        while queue:
            current = queue.pop(0)
            if current[-1] == destination: # If current path ends at the destination, return path
                return current

            for country in self.routes[current[-1]]: # Loop through countries adjacent to the last country in the current path
                if country not in visited: # If country hasn't been visited, add it to the current path and add the path to the queue
                    visited.append(country)
                    queue.append(current + [country])
                    

        return None # Error when finding route

class Controller:
    def __init__(self):
        '''
        Instantiate Flask web framework object, DeliveryRoutes() to find the path, and add url rule
        to receive destination country code
        '''
        self.app = Flask(__name__)
        self.delivery = DeliveryRoutes()
        self.app.add_url_rule('/<country_code>', 'find_route', self.find_route)
    
    def find_route(self, country_code: str) -> Response:
        '''
        Handle route and return it to web server as a Json object
        '''
        country_code = country_code.upper() #ensure a valid format for country code
        route = self.delivery.find_route("USA", country_code) # generate route from USA to destination country

        # if route exits, return Json object representing the destination and the path
        if route:
            return jsonify({
                "destination": country_code,
                "list": route
            })
        else:
            return jsonify({
                "error": "Invalid country code"
            })

    def run(self) -> None:
        '''
        Call run on the Flask object
        '''
        
        serve(self.app, port=8080)

if __name__ == '__main__':
    controller = Controller()
    controller.run()