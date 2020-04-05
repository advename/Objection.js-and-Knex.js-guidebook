const express = require("express");
const router = express.Router();
const Todo = require("../../models/Todos.js");

// Create endpoint of all todos
router.get("/", async (req, res) => {
  const todos = await Todo.query().withGraphFetched("user");
  return res.json(todos);
});

// Export to api.js
module.exports = router;
