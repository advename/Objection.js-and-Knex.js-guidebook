// Executed during a migration
exports.up = function(knex) {
  return knex.schema
    .createTable("users", table => {
      table.increments("id");
      table.string("name").notNullable();
      table.integer("age");
    })
    .createTable("todos", table => {
      table.increments("id");
      table.string("todo").notNullable();
      table.boolean("done").defaultTo(false);
      table
        .integer("user_id")
        .unsigned()
        .notNullable();

      table
        .foreign("user_id")
        .references("id")
        .inTable("users")
        .onDelete("CASCADE")
        .onUpdate("CASCADE");
    });
};

// Executed during a rollback
exports.down = function(knex) {
  return (
    knex.schema
      // Here, delete tables in reverse order because todos depends on users
      .dropTableIfExists("todos")
      .dropTableIfExists("users")
  );
};
