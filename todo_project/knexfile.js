const credentials = require("./config/db_config.js");

module.exports = {
  development: {
    client: "mysql",
    connection: {
      host: credentials.host,
      database: credentials.database,
      user: credentials.user,
      password: credentials.password
    }
    // debug: true
  }
};
