const express = require("express");
const app = express();

// Require router files
const usersRoutes = require("./api/users");
const todosRoutes = require("./api/todos");

// Include the routes to express
app.use("/users", usersRoutes);
app.use("/todos", todosRoutes);

// Export the file to be used in server.js
module.exports = app;
