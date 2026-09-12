DELETE p1 FROM 
Person p1
JOIN Person p2 ON 
    p1.email = p2.email   -- p1.id1 will have combinations with 2; as p2 has id 1 and 3 matched with p1.id1 
WHERE p1.id > p2.id
