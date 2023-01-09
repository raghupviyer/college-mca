const fetchAndAddTodo = async () => {
  const result = await (await fetch('https://jsonplaceholder.typicode.com/todos/1')).json()
  console.log(result)
}

// u can add async keyword even before a class

(async () => {
  try {
    const result = await (await fetch('https://jsonplaceholder.typicode.com/todos/1')).json()
    console.log(result)
  } catch (error) {
    console.log(error);
  }
})();