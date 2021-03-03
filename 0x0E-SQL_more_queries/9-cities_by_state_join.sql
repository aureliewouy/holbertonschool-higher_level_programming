-- Lists all the cities and its states
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;
