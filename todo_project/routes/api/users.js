const express = require("express");
const router = express.Router();

// Custom error handler
const inputError = require("../../helpers/error.js");

// Import User class from models
const User = require("../../models/Users");

// Create endpoint of all users
router.get("/", async (req, res) => {
  const users = await User.query();
  return res.json(users);
});

router.post("/", async (req, res) => {
  const { name, age } = req.body;

  try {
    const user = await User.query().insert({ name, age });
    return res.json(user);
  } catch (err) {
    // Create a schema for each fields possible error messages
    let keyErrors = {
      name: {
        required: "Name field is required",
        minLength: "Name too short",
        maxLength: "Name too long",
        type: "Name incorrect type"
      },
      age: {
        type: "Age incorrect type"
      }
    };

    // Save the returned error messages
    let errorMessages = inputError(err, keyErrors);

    return res.status(404).json(errorMessages);
  }
});

// Export to api.js
module.exports = router;

/**
 * The output i receive in Postman is:
 * [
 *    "Name field is required",
 *    "Age incorrect type"
 * ]
 */
