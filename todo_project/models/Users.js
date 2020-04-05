// Import Model class from Objection.js
const { Model } = require("objection");

// Create the User model class
class User extends Model {
  static get tableName() {
    return "users";
  }

  static get jsonSchema() {
    return {
      type: "object",
      required: ["name"],

      properties: {
        id: { type: "integer" },
        name: { type: "string", minLength: 1, maxLength: 255 },
        age: { type: "number" } //optional
      }
    };
  }
}

// Export the User to be used in routes
module.exports = User;
