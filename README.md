# North American Country Route API

## Overview

Web API built using Flask and Python that allows users to find the route a driver must travel to go from the United States of America to a specified North American country. Utilizing a simplified map of North America, the API supports requests for routes based on three-letter country codes and returns the path from the United States to the given country.

## Features

- **Endpoint for Route Retrieval**: Users can send a request with a three-letter country code and receive a list of all countries that must be traversed to reach the destination from the USA.
- **Breadth-First Search (BFS) Algorithm**: The API implements a BFS algorithm to find the shortest path through the countries.
- **Error Handling**: If an invalid country code is provided, the API returns an appropriate error message.

## Country Codes and Connections

List of supported countries (code is structured to easily support addition of more countries):

- **USA** – Borders Canada and Mexico
- **CAN** – Borders the USA
- **MEX** – Borders the USA, Guatemala, and Belize
- **BLZ** – Borders Mexico and Guatemala
- **GTM** – Borders Mexico, Belize, El Salvador, and Honduras
- **SLV** – Borders Guatemala and Honduras
- **HND** – Borders Guatemala, El Salvador, and Nicaragua
- **NIC** – Borders Honduras and Costa Rica
- **CRI** – Borders Nicaragua and Panama
- **PAN** – Borders Costa Rica

## API Endpoints

### Retrieve Route

- **Endpoint**: `GET /<country_code>`
  
  **Example Requests**:
  - `GET /PAN` -> Returns the route: `["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]`
  - `GET /BLZ` -> Returns the route: `["USA", "MEX", "BLZ"]`
  - `GET /USA` -> Returns the route: `["USA"]`
  
  **Response Format**:
  ```json
  {
      "destination": "PAN",
      "list": ["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]
  }
