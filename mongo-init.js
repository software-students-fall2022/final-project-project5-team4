db = db.getSiblingDB("containerizedTest");

db.sentiments.insertMany([
    {text: 'Today is a wonderful day, and I have a good modd', isPositive: true, positive_words: ['wonderful', 'good'], negative_words: [], createdDate: '2022-12-01'},
    {text: 'I am so sorry about this', isPositive: false, positive_words: [], negative_words: ['sorry'], createdDate: '2022-12-02'}
]);
