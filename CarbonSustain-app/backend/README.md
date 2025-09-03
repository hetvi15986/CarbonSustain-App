CarbonSustain Coding Assignment: Backend API

Purpose: REST API to manage and track sustainability actions with CRUD functionality, using a database model stored in a JSON file.

Functions:
GET Endpoint: Retrieve a list of all sustainability actions.
    (URL: /api/actions/)
    
POST Endpoint: Add a new sustainability action. 
    (URL: /api/actions/)

    Payload format: { "action": "Recycling", "date": "2025-01-08", "points": 25 }
    
PUT/PATCH Endpoint: Update an existing action 
    (URL: /api/actions/<id>/)
    
DELETE Endpoint: Delete and action 
    (URL: /api/actions/<id>/)
    
All data persists in backend/action.json JSON file
