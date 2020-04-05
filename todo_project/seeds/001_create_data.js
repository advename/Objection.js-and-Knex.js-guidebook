exports.seed = function(knex) {
  // Deletes ALL data of todos
  return knex("todos")
    .del()
    .then(() => {
      //Delete ALL data of users
      return knex("users").del();
    })
    .then(() => {
      //Inserts new data into users
      return knex("users").insert([
        {
          name: "Marc",
          age: 19
        },
        {
          name: "Ben",
          age: 31
        },
        {
          name: "Jessica",
          age: 27
        }
      ]);
    })
    .then(users => {
      /**
       * We can use the callback of the previous users inserts,
       * which returns a single item or an array of items (array only available in PostgressSQL), to
       * insert todos data and establish the relationship to users.
       */
      return knex("todos").insert([
        {
          user_id: 1, //-> Marc
          // alternatively to the fixed value one, you can also use
          // user_id: users[0]
          todo: "Buy Milk"
        },
        {
          user_id: 1, //-> Marc
          todo: "Walk the dog"
        },
        {
          user_id: 2, //-> Jessica
          todo: "Call grandma"
        }
      ]);
    });
};
