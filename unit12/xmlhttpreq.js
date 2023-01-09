const xhr = new XMLHttpRequest();
// xhr is also an event target, which means there 
// will be some events which will fire on this
//readyStateChange, load are events which will fire on this


xhr.onload = function () {
  console.log(xhr.responseText);
}

/**
 * whenn the request gets a response
 * then this finction will execute
 */

xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1')
xhr.send();