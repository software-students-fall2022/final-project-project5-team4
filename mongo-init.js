db = db.getSiblingDB("containerizedTest");

db.users.insertOne(
    {username: 'admin', password: 'password', email:'admin@gmail.com', favorite_apt: 0}
);
db.reviews.insert_one(
    {comments: 'comments', rating: 0, added_at: 0, address_id: 5}
);