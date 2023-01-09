fetch('https://jsonplaceholder.typicode.com/todos/1')
.then(  req => req.json())
.then(  result => console.log(result))
.catch(  e => console.log(e))

fetch('https://jsonplaceholder.typicode.com/todos/1',{
  method: 'POST',
  body: JSON.stringify({
    "userId": 1,
    "title": "delectus aut autem",
    "completed": false
  }),
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(  req => req.json())
.then(  result => console.log(result))
.catch(  e => console.log(e))