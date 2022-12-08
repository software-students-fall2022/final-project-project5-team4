db = db.getSiblingDB("containerizedTest");

db.users.insertOne(
    {username: 'admin', password: 'password', email:'admin@gmail.com', favorite_apt: 0}
);
