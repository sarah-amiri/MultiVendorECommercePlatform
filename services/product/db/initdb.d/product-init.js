db = db.getSiblingDB("product_db")

db.createUser({
    user: "user",
    pwd: "pass",
    roles: [
        {
            role: 'readWrite',
            db: 'product_db'
        }
    ]
});