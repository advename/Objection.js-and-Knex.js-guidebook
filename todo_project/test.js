// 1. Import and initialize Knex.js
const Knex = require("knex");
const knexFile = require("./knexfile.js");
const knex = Knex(knexFile.development);

// 2. Import Objection.js Model class
const { Model } = require("objection");

// 3. Apply the knex instance to it
Model.knex(knex);

// 4. Create the User model class
class User extends Model {
  static get tableName() {
    return "users";
  }
}

// 5. Run the query in async/await
const getUsers = async () => {
  const users = await User.query();
  console.log(users);
};
getUsers();
