db = db.getSiblingDB("containerizedTest");

db.users.insertOne(
    {username: 'admin', password: 'password', email:'admin@gmail.com', favorite_apt:[]}
);

db.apartments.insertOne(
    { 
        "name": "The Octagon",
        "address": "888 Main St",
        "borough": "Roosevelt Island",
        "photo":"https://thumbs.cityrealty.com/assets/smart/736x/webp/9/97/9788674e147c90430c2beb67a1ec17e6297df3af/octagon-rotunda.jpg",
        "year_of_construction": 2001,
        "price": 10000,
        "pet_friendly": true,
        "doorman": false,
        "gym": true,
        "parking": false,
        "elevator": true,
        "laundry_in_building": true
    }
);

db.reviews.insertOne(
    {comments: 'comments', rating: 0, added_at: 0, address_id: 5}
);