function inputError(errData, keyErrors) {
  // Initialize empty error array
  let errorMessage = [];

  // Loop through all keys in the error message
  for (let key in errData) {
    // Get the error type keyword
    const keyword = errData[key][0].keyword;
    // Get the keys keyword error message and push to error message array
    errorMessage.push(keyErrors[key][keyword]);
  }

  return errorMessage;
}

// Export the Todo to be used in routes
module.exports = inputError;
